import socket
import struct
import json
import os.path
from Module.ftp import *

if __name__ == '__main__':
    session=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    session.bind(('127.0.0.1',8081))
    session.listen(5)

    while True:
        conn, client_addr = session.accept()

        while True:
            try:
                cmd=conn.recv(1024)
                cmd_decode=cmd.decode('utf-8')
                if not cmd_decode:break

                command_lst=cmd_decode.split(' ')
                command_args=command_lst[0]
                filename_r=command_lst[1]
                filename_w=command_lst[1].split('\\').pop()

                if command_args == 'get':
                    if not os.path.exists(filename_r):
                        msg='文件不存在'
                        conn.send(struct.pack('i',len(msg.encode('utf-8'))))
                        conn.send(msg.encode('utf-8'))
                        continue
                    file=Ftp(filename_r)
                    data_dict=file.get()
                    data=data_dict['file_data']
                    del data_dict['file_data']
                    # print(data_dict['file_type'])

                    data_json=json.dumps(data_dict)
                    data_json_bytes=data_json.encode('utf-8')

                    conn.send(struct.pack('i',len(data_json_bytes)))
                    conn.send(data_json_bytes)
                    if data_dict['file_type'] == "<class 'bytes'>":
                        conn.send(data)
                    else:
                        conn.send(data.encode('utf-8'))
                else:
                    msg_size = 0
                    msg = b''
                    data_size = 0
                    data = b''
                    msg_total_size=struct.unpack('i',conn.recv(4))[0]
                    if msg_total_size <= 1024:
                        msg = conn.recv(msg_total_size)
                        if msg.decode('utf-8') == '文件不存在':
                            print('文件不存在')
                            continue
                    else:
                        while msg_size < msg_total_size:
                            msg_split=conn.recv(1024)
                            msg+=msg_split
                            msg_size+=len(msg_split)

                    msg_dic = json.loads(msg.decode('utf-8'))

                    if msg_dic['file_type'] == "<class 'bytes'>":
                        total_size = msg_dic['file_size']

                        if total_size <= 10240:
                            data = conn.recv(total_size)
                            print('传输已完成100%')
                        else:
                            while data_size < total_size:
                                data_split = conn.recv(10240)
                                data += data_split
                                data_size += len(data_split)
                                print(f'传输已完成{len(data) / total_size:.2%}')
                        with open(filename_w, 'wb') as wfile:
                            wfile.write(data)
                    else:
                        total_size = msg_dic['file_size']

                        if total_size <= 10240:
                            data = conn.recv(total_size)
                            print('传输已完成100%')
                        else:
                            while data_size < total_size:
                                data_split = conn.recv(10240)
                                data += data_split
                                data_size += len(data_split)
                                print(f'传输已完成{len(data)/total_size:.2%}')
                        with open(filename_w,'w') as wfile:
                            wfile.write(data.decode('utf-8'))

            except Exception as e:
                print(e)
                msg = '文件不存在'
                conn.send(struct.pack('i', len(msg.encode('utf-8'))))
                conn.send(msg.encode('utf-8'))
                continue

        conn.close()

    session.close()