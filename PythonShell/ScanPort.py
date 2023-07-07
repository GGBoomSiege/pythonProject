import socket
import threading

def scan_ports(host, port_list):
    for port in port_list:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 设置超时时间为1秒
            result = sock.connect_ex((host, int(port)))
            if result == 0:
                print(f"端口 {port} 开放")
            # else:
            #     print(f"端口 {port} 关闭")
            sock.close()
        except socket.error:
            print(f"无法连接到主机 {host}")

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 设置超时时间为1秒
        result = sock.connect_ex((host, int(port)))
        if result == 0:
            print(f"端口 {port} 开放")
        # else:
        #     print(f"端口 {port} 关闭")
        sock.close()
    except socket.error:
        print(f"无法连接到主机 {host}")

if __name__ == '__main__':
    target_host = input("请输入目标主机的IP地址或主机名：")
    target_ports = input("请输入要扫描的目标端口号：")
    port_list = list(range(int(target_ports.split('-')[0]), int(target_ports.split('-')[1]) + 1))
