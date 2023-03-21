import socket
import struct
import json
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
                filename=command_lst[1]

                if command_args == 'get':
                    if not os.path.exists(filename):
                        print('文件不存在')
                        continue
                    file=Ftp(filename)
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

                elif command_args == 'put':
                    pass
                else:
                    pass

            except Exception as e:
                print(e)
                continue

        conn.close()

    session.close()