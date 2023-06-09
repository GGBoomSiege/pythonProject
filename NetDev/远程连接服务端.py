import socket
import subprocess
import struct
import json

if __name__ == '__main__':
    phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    phone.bind(('127.0.0.1',8081))

    phone.listen(5) #最大挂起的连接数

    while True:
        conn, client_addr = phone.accept()

        while True:
            try:
                cmd=conn.recv(1024)
                cmd_decode=cmd.decode('utf-8')
                if not cmd_decode:break

                msg=subprocess.Popen(
                    cmd_decode,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True
                )

                stdout=msg.stdout.read()
                stderr=msg.stderr.read()

                total_size=len(stdout)+len(stderr)

                msg_dic={
                    'name':'test.py',
                    'md5':'12345678',
                    'total_size':total_size
                }

                msg_json=json.dumps(msg_dic)
                msg_bytes=msg_json.encode('utf-8')

                conn.send(struct.pack('i',len(msg_bytes)))
                conn.send(msg_bytes)

                # conn.send(struct.pack('i',total_size))
                conn.send(stdout)
                conn.send(stderr)

            except Exception as e:
                break

        conn.close()

    phone.close()