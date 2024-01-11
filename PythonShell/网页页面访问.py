import requests
from concurrent.futures import ThreadPoolExecutor
import time


# HTTP请求函数
def http_request(url, method, data, headers):
    global http_content
    if method.upper() == "GET":
        response = requests.get(url, headers=headers)
    elif method.upper() == "POST":
        response = requests.post(url, headers=headers, data=data)
    http_content.append(
        (
            response.text,
            response.headers,
            response.cookies,
            response.status_code,
        )
    )


# 多线程
def httpRequest_tasks(tasks):
    with ThreadPoolExecutor(max_workers=10000) as executor:
        for task in tasks:
            executor.submit(http_request, task[0], task[1], task[2], task[3])


if __name__ == "__main__":
    # url = "http://192.168.12.122:1003/ndaesp/apps/exchange/app/sso/DejaxUser/login"
    # method = "post"
    # data = {
    #     "usertype": "ep",
    #     "loginname": "admin",
    #     "loginpass": "JTVCMC4zNzQ4NDY4OTE5MDM3OTU3JTJDJTIyMTIzJTIyJTJDMTcwMzc1MTUwODQ3OCU1RA==",
    # }
    http_content = []

    dataLst = [
        (
            "http://192.168.12.122:1003/ndaesp/apps/exchange/app/sso/DejaxUser/login",
            "post",
            {
                "usertype": "ep",
                "loginname": "admin",
                "loginpass": "JTVCMC4zNzQ4NDY4OTE5MDM3OTU3JTJDJTIyMTIzJTIyJTJDMTcwMzc1MTUwODQ3OCU1RA==",
            },
        ),
        (
            "https://www.baidu.com",
            "get",
            {},
        ),
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    }

    # 定义任务列表
    tasks = []
    for data in dataLst:
        task = (data[0], data[1], data[2], headers)
        tasks.append(task)

    # 执行任务列表
    start_time = time.time()
    print(f"正在进行页面访问......")
    httpRequest_tasks(tasks)
    end_time = time.time()

    # 打印页面访问信息
    for item in http_content:
        print(item[0])
        print(item[1])
        print(item[2])
        print(item[3])
        print()
    print(f"脚本运行总计耗时：{ end_time - start_time }秒")
