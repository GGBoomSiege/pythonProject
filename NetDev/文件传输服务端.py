import socket
import struct
import json
import os
from Module.ftp import *

if __name__ == '__main__':
    session=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    session.bind(('127.0.0.1',8081))

    session.listen(5) #最大挂起的连接数

    while True:
        conn, client_addr = session.accept()

        while True:
            try:
                cmd=conn.recv(1024)
                cmd_decode=cmd.decode('utf-8')
                if not cmd_decode:break

                command_lst=cmd_decode.split(' ')
                command_args=command_lst[0]
                filename=command_lst[1]

                if command_args == 'get':
                    if not os.path.exists(filename):
                        print('文件不存在')
                        continue
                    file=Ftp(filename)
                    data_dict=file.get()
                    data=data_dict['file_data']
                    del data_dict['file_data']
                    print(data_dict['file_type'])

                    data_json=json.dumps(data_dict)
                    data_json_bytes=data_json.encode('utf-8')

                    conn.send(struct.pack('i',len(data_json_bytes)))
                    conn.send(data_json_bytes)
                    # conn.send(data)

                elif command_args == 'put':
                    pass
                else:
                    pass

                # stdout=msg.stdout.read()
                # stderr=msg.stderr.read()
                #
                # total_size=len(stdout)+len(stderr)
                #
                # msg_dic={
                #     'name':'test.py',
                #     'md5':'12345678',
                #     'total_size':total_size
                # }
                #
                # msg_json=json.dumps(msg_dic)
                # msg_bytes=msg_json.encode('utf-8')
                #
                # conn.send(struct.pack('i',len(msg_bytes)))
                # conn.send(msg_bytes)
                #
                # # conn.send(struct.pack('i',total_size))
                # conn.send(stdout)
                # conn.send(stderr)

            except Exception as e:
                print(e)
                continue

        conn.close()

    session.close()