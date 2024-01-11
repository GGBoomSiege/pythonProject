import argparse
from concurrent.futures import ThreadPoolExecutor
import socket
import time


# 端口扫描函数
def scan_port(ip, port):
    global open_ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        open_ports.append(port)
    sock.close()


# 多线程
def scan_tasks(tasks):
    with ThreadPoolExecutor(max_workers=10000) as executor:
        for task in tasks:
            executor.submit(scan_port, task[0], task[1])


def scanPorts(ip, ports):
    global open_ports
    tasks = []
    task = ()

    # tasks = [("scan_port", "192.168.12.123", 22), ("scan_port", "192.168.12.123", 25)]

    # 定义任务列表
    for port in range(int(ports[0]), int(ports[1])):
        task = (ip, port)
        tasks.append(task)

    # 执行任务列表
    start_time = time.time()
    print(f"正在扫描主机 {ip} 的可用端口......")
    scan_tasks(tasks)
    end_time = time.time()

    print(f"开放的端口有：{open_ports}")
    print(f"脚本运行时间：{ end_time - start_time }秒")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="多线程端口扫描脚本")
    parser.add_argument(
        "--host", type=str, default="192.168.12.123", help="请输入需要扫描的主机地址"
    )
    parser.add_argument(
        "--ports",
        type=str,
        default="1-65535",
        help="请输入需要扫描的端口组，如：1-65535",
    )
    args = parser.parse_args()

    open_ports = []

    args = parser.parse_args()

    ip = args.host
    ports = args.ports.split("-")
    scanPorts(ip, ports)
