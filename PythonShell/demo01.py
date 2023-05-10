import requests
import json
from multiprocessing import Process

def run(code):

    url = f'https://proxy.finance.qq.com/cgi/cgi-bin/fundflow/hsfundtab?code={code}&type=historyFundFlow,fiveDayFundFlow,todayFundTrend,todayFundFlow&klineNeedDay=20'

    res = requests.get(url).text

    data_dict = json.loads(res)["data"]["todayFundTrend"]["minList"]

    print(data_dict)

if __name__ == '__main__':
    filename = './data/code.txt'
    with open(filename, 'r') as rfile:
        codes = rfile.readlines()

    for item in codes:
        run(item.strip())