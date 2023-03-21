import socket
import struct
import json
from Module.ftp import *

if __name__ == '__main__':
    session=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    session.connect(('127.0.0.1',8081))

    while True:
        msg_size=0
        msg=b''
        data_size=0
        data=b''
        cmd=input('>>:').strip()
        if cmd=='quit':break
        if not cmd:continue
        if len(cmd.split(' ')) != 2 or cmd.split(' ')[0] not in ['get','put']:
            print('格式错误,请重新输入...')
            continue
        filename_r=cmd.split(' ')[1]
        filename_w=cmd.split(' ')[1].split('\\').pop()

        session.send(cmd.encode('utf-8'))

        if cmd.split(' ')[0] == 'get':
            msg_total_size=struct.unpack('i',session.recv(4))[0]

            if msg_total_size <= 1024:
                msg=session.recv(msg_total_size)
                if msg.decode('utf-8') == '文件不存在':
                    print('文件不存在')
                    continue
            else:
                while msg_size < msg_total_size:
                    msg_split=session.recv(1024)
                    msg+=msg_split
                    msg_size+=len(msg_split)

            msg_dic=json.loads(msg.decode('utf-8'))

            # print(msg_dic)
            if msg_dic['file_type'] == "<class 'bytes'>":
                # print('yes')
                total_size = msg_dic['file_size']

                if total_size <= 10240:
                    data = session.recv(total_size)
                    print('传输已完成100%')
                else:
                    while data_size < total_size:
                        data_split = session.recv(10240)
                        data += data_split
                        data_size += len(data_split)
                        print(f'传输已完成{len(data)/total_size:.2%}')
                with open(filename_w,'wb') as wfile:
                    wfile.write(data)

            else:
                # print('no')
                total_size = msg_dic['file_size']

                if total_size <= 10240:
                    data = session.recv(total_size)
                    print('传输已完成100%')
                else:
                    while data_size < total_size:
                        data_split = session.recv(10240)
                        data += data_split
                        data_size += len(data_split)
                        print(f'传输已完成{len(data)/total_size:.2%}')
                with open(filename_w,'w') as wfile:
                    wfile.write(data.decode('utf-8'))
        else:
            if not os.path.exists(filename_r):
                msg = '文件不存在'
                session.send(struct.pack('i', len(msg.encode('utf-8'))))
                session.send(msg.encode('utf-8'))
                continue
            file = Ftp(filename_r)
            data_dict = file.get()
            file_data = data_dict['file_data']
            del data_dict['file_data']

            data_json = json.dumps(data_dict)
            data_json_bytes = data_json.encode('utf-8')

            session.send(struct.pack('i', len(data_json_bytes)))
            session.send(data_json_bytes)

            if data_dict['file_type'] == "<class 'bytes'>":
                session.send(file_data)
            else:
                session.send(file_data.encode('utf-8'))

    session.close()