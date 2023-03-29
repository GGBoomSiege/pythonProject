import requests

url = 'https://www.opcloud.cn/v2/api/opcloud/sys/signIn?username=liujun_666&orgNumber=666&password=123456_&grant_type=password&client_id=opcloud&client_secret=1'
# url = 'http://httpbin.org/post'

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
    'cookie': '_ga=GA1.2.485151833.1659319101; __bid_n=183bfa9d2ab7def3b44207; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22183bfa9d2f2752-045232ebd5e299-7b555471-1327104-183bfa9d2f3a5e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22183bfa9d2f2752-045232ebd5e299-7b555471-1327104-183bfa9d2f3a5e%22%7D; Hm_lvt_c73e7733487a7ce0e2d4bd3efab1918b=1665367921,1665462468,1665538564,1665990151; _gid=GA1.2.1222201688.1679967062'
}

data = {
    'username': 'liujun_666',
    'orgNumber': '666',
    'password': '123456_',
    'grant_type': 'password',
    'client_id': 'opcloud',
    'client_secret': '1'
}

res=requests.get(url,data=data,headers=headers)

res.encoding='utf-8'

print(res.text)