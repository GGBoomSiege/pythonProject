from Module.ftp import *

if __name__ == '__main__':
    session=Session('127.0.0.1',8081)
    session.listen(5)

    while True:
        while True:
            operation=session.receive(1024)
            operation_decode=operation.decode('utf-8')
            if not operation_decode:break

            command_lst=operation_decode.split(' ')
            command_args=command_lst[0]
            filename_r=command_lst[1]
            filename_w=command_lst[1].split('\\').pop()

            if command_args == 'get':
                if not session.ftp_send(filename_r):continue
            elif command_args == 'put':
                if not session.ftp_receive(filename_w):continue

        session.accept_close()

    session.session_close()