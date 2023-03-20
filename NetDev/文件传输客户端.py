import socket
import struct
import json

if __name__ == '__main__':
    phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    phone.connect(('127.0.0.1',8081))

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

        phone.send(cmd.encode('utf-8'))

        msg_total_size=struct.unpack('i',phone.recv(4))[0]

        if msg_total_size <= 1024:
            msg=phone.recv(msg_total_size)
        else:
            while msg_size < msg_total_size:
                msg_split=phone.recv(1024)
                msg+=msg_split
                msg_size+=len(msg_split)

        msg_dic=json.loads(msg.decode('utf-8'))

        print(msg_dic)
        if msg_dic['file_type'] == "<class 'bytes'>":
            print('yes')
        else:
            print('no')
        # total_size= msg_dic['total_size']
        #
        # while data_size < total_size:
        #     data_split=phone.recv(1024)
        #     data+=data_split
        #     data_size+=len(data_split)
        #
        # print(data.decode('gbk'))

    phone.close()