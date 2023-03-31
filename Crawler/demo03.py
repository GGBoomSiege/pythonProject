import hashlib
import time

keyword = input('请输入要查询的歌曲信息:')

text = [
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
    "appid=1014",
    "bitrate=0",
    "callback=callback123",
    "clienttime=1680059448649",
    "clientver=1000",
    "dfid=1bmguz1ka3uc1f09CB3leCa8",
    "filter=10",
    "inputtype=0",
    "iscorrection=1",
    "isfuzzy=0",
    f"keyword={keyword}",
    "mid=7d2c08b54d7703de1e5775d9069e1efa",
    "page=1",
    "pagesize=30",
    "platform=WebFilter",
    "privilege_filter=0",
    "srcappid=2919",
    "token=",
    "userid=0",
    "uuid=7d2c08b54d7703de1e5775d9069e1efa",
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
]
var = "".join(text)
md5 = hashlib.md5(var.encode(encoding='utf-8')).hexdigest()

print(md5)