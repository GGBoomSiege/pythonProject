from socket import *

client=socket(AF_INET,SOCK_DGRAM)

while True:
    try:
        msg=input('>>:').strip()
        client.sendto(msg.encode('utf-8'),('127.0.0.1',8080))

        data=client.recvfrom(1024)
        print(data)
    except Exception as e:
        print(e)

server.close()