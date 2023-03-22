import os
import magic
import re
import codecs
import socket
import struct
import json

def is_binary_file_1(ff):

    TEXT_BOMS = (
        codecs.BOM_UTF16_BE,
        codecs.BOM_UTF16_LE,
        codecs.BOM_UTF32_BE,
        codecs.BOM_UTF32_LE,
        codecs.BOM_UTF8,
    )
    with open(ff, 'rb') as file:
        CHUNKSIZE = 8192
        initial_bytes = file.read(CHUNKSIZE)
        file.close()
    #: BOMs to indicate that a file is a text file even if it contains zero bytes.
    return not any(initial_bytes.startswith(bom) for bom in TEXT_BOMS) and b'\0' in initial_bytes

def is_binwary_file_2(ff):
    mime_kw = 'x-executable|x-sharedlib|octet-stream|x-object'  ###可执行文件、链接库、动态流、对象
    try:
        magic_mime = magic.from_file(ff, mime=True)
        magic_hit = re.search(mime_kw, magic_mime, re.I)
        if magic_hit:
            return True
        else:
            return False
    except Exception as e:
        return False

class Ftp:
    def __init__(self,filename):
        self.filename=filename

    def get(self):
        file_list1=['file_size','file_type','file_data']
        file_list2=[]
        if any((is_binary_file_1(self.filename), is_binwary_file_2(self.filename))):
            with open(self.filename,'rb') as rfile:
                data=rfile.read()
                file_list2.append(len(data))
                file_list2.append(str(type(data)))
                file_list2.append(data)
                file_dict={file_list1:file_list2 for file_list1,file_list2 in zip(file_list1,file_list2)}
                return file_dict
        else:
            with open(self.filename,'r',encoding='utf-8') as rfile:
                data = rfile.read()
                file_list2.append(len(data))
                file_list2.append(str(type(data)))
                file_list2.append(data)
                file_dict = {file_list1: file_list2 for file_list1, file_list2 in zip(file_list1, file_list2)}
                return file_dict

class Session:
    def __init__(self,IPADDR, PNUM):
        self.IPADDR=IPADDR
        self.PNUM=PNUM
        self.SESSION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self, SNUM):
        self.SESSION.bind((self.IPADDR, self.PNUM))
        self.SESSION.listen(SNUM)
        self.CONN, self.client_addr = self.SESSION.accept()

    def connect(self):
        self.SESSION.connect((self.IPADDR, self.PNUM))
        self.CONN=self.SESSION

    def receive(self, BYTES):
        return self.CONN.recv(BYTES)

    def accept_close(self):
        self.CONN.close()

    def session_close(self):
        self.SESSION.close()

    def ftp_send(self,FILENAME):
        try:
            if not os.path.exists(FILENAME):
                msg = '文件不存在'
                self.CONN.send(struct.pack('i', len(msg.encode('utf-8'))))
                self.CONN.send(msg.encode('utf-8'))
                return False
            file = Ftp(FILENAME)
            data_dict = file.get()
            data = data_dict['file_data']
            del data_dict['file_data']

            data_json = json.dumps(data_dict)
            data_json_bytes = data_json.encode('utf-8')

            self.CONN.send(struct.pack('i', len(data_json_bytes)))
            self.CONN.send(data_json_bytes)
            if data_dict['file_type'] == "<class 'bytes'>":
                self.CONN.send(data)
            else:
                self.CONN.send(data.encode('utf-8'))
        except Exception as e:
            print(e)
            msg = '文件不存在'
            self.CONN.send(struct.pack('i', len(msg.encode('utf-8'))))
            self.CONN.send(msg.encode('utf-8'))

    def ftp_receive(self,FILENAME):
        try:
            msg_size = 0
            msg = b''
            data_size = 0
            data = b''
            msg_total_size = struct.unpack('i', self.CONN.recv(4))[0]
            if msg_total_size <= 1024:
                msg = self.CONN.recv(msg_total_size)
                if msg.decode('utf-8') == '文件不存在':
                    print('文件不存在')
                    return False
            else:
                while msg_size < msg_total_size:
                    msg_split = self.CONN.recv(1024)
                    msg += msg_split
                    msg_size += len(msg_split)

            msg_dic = json.loads(msg.decode('utf-8'))

            if msg_dic['file_type'] == "<class 'bytes'>":
                total_size = msg_dic['file_size']

                if total_size <= 10240:
                    data = self.CONN.recv(total_size)
                    print('传输已完成100%')
                else:
                    while data_size < total_size:
                        data_split = self.CONN.recv(10240)
                        data += data_split
                        data_size += len(data_split)
                        print(f'传输已完成{len(data) / total_size:.2%}')
                with open(FILENAME, 'wb') as wfile:
                    wfile.write(data)
            else:
                total_size = msg_dic['file_size']

                if total_size <= 10240:
                    data = self.CONN.recv(total_size)
                    print('传输已完成100%')
                else:
                    while data_size < total_size:
                        data_split = self.CONN.recv(10240)
                        data += data_split
                        data_size += len(data_split)
                        print(f'传输已完成{len(data) / total_size:.2%}')
                with open(FILENAME, 'w') as wfile:
                    wfile.write(data.decode('utf-8'))
        except Exception as e:
            print(e)
            msg = '文件不存在'
            self.CONN.send(struct.pack('i', len(msg.encode('utf-8'))))
            self.CONN.send(msg.encode('utf-8'))