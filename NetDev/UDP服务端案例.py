from socket import *

server=socket(AF_INET,SOCK_DGRAM)

server.bind(('127.0.0.1',8080))

while True:
    try:
        data,client_addr=server.recvfrom(2)
        print(data)

        server.sendto(data.upper(),client_addr)
    except Exception as e:
        print(e)

server.close()