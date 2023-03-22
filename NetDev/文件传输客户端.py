from Module.ftp import *

if __name__ == '__main__':
    session=Session('127.0.0.1',8081)
    session.connect()

    while True:
        operation=input('>>:').strip()
        if operation=='quit':break
        if not operation:continue
        if len(operation.split(' ')) != 2 or operation.split(' ')[0] not in ['get','put']:
            print('格式错误,请重新输入...')
            continue
        filename_r=operation.split(' ')[1]
        filename_w=operation.split(' ')[1].split('\\').pop()

        session.SESSION.send(operation.encode('utf-8'))

        if operation.split(' ')[0] == 'get':
            if not session.ftp_receive(filename_w): continue
        elif operation.split(' ')[0] == 'put':
            if not session.ftp_send(filename_r): continue

    session.close()