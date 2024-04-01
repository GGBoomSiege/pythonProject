from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from itertools import zip_longest

import datetime
import uuid
import time
import yaml


def getBT(word):
    # 创建一个webdriver对象，指定浏览器类型和驱动程序路径
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--ignore-certificate-errors")
    service = webdriver.chrome.service.Service(
        executable_path=r"E:\Python\Python312\chromedriver.exe"
    )
    service_log_path = "chromedriver.log"
    service.service_log_path = service_log_path

    driver = webdriver.Chrome(options=options, service=service)
    driver.set_window_size(1920, 1080)
    # driver.minimize_window()

    # 打开目标网页
    url = f"http://clm15.work/search?word={word}"
    driver.get(url)
    time.sleep(10)
    driver.close()


if __name__ == "__main__":
    getBT("三枪拍案惊奇")
