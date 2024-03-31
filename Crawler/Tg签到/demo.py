import yaml
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time

configPath = "./Crawler/Tg签到/config.yaml"
storagePath = "./Crawler/Tg签到/storage.yaml"


def getStorage(url):
    # 创建一个webdriver对象，指定浏览器类型和驱动程序路径
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # options = webdriver.ChromeOptions()
    # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    # options.add_argument("--remote-debugging-port=9922")
    # options.add_argument("--remote-debugging-address=127.0.0.1")
    # options.add_argument(f"user-agent={user_agent}")
    # options.add_argument("--ignore-certificate-errors")
    # service = webdriver.chrome.service.Service(
    #     executable_path=r"E:\Python\Python312\chromedriver.exe"
    # )
    # service_log_path = "chromedriver.log"
    # service.service_log_path = service_log_path
    # driver = webdriver.Chrome(options=options, service=service)

    # 接管外部浏览器
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9922")
    driver = webdriver.Chrome(options=options)

    # driver.set_window_size(1920, 1080)
    # driver.minimize_window()

    # 打开目标网页
    # driver.get(url)
    driver.get(f"https://web.telegram.org/a/#6042960290")

    GramJs_apiCache = driver.execute_script(
        "return window.localStorage.getItem('GramJs:apiCache')"
    )
    dc2_hash = driver.execute_script("return window.localStorage.getItem('dc2_hash')")
    user_auth = driver.execute_script("return window.localStorage.getItem('user_auth')")
    dc = driver.execute_script("return window.localStorage.getItem('dc')")
    dc5_hash = driver.execute_script("return window.localStorage.getItem('dc5_hash')")
    dc4_auth_key = driver.execute_script(
        "return window.localStorage.getItem('dc4_auth_key')"
    )
    dc2_auth_key = driver.execute_script(
        "return window.localStorage.getItem('dc2_auth_key')"
    )
    dc5_auth_key = driver.execute_script(
        "return window.localStorage.getItem('dc5_auth_key')"
    )
    tgme_sync = driver.execute_script("return window.localStorage.getItem('tgme_sync')")
    kz_version = driver.execute_script(
        "return window.localStorage.getItem('kz_version')"
    )
    dc1_auth_key = driver.execute_script(
        "return window.localStorage.getItem('dc1_auth_key')"
    )
    tt_global_state = driver.execute_script(
        "return window.localStorage.getItem('tt-global-state')"
    )
    dc1_hash = driver.execute_script("return window.localStorage.getItem('dc1_hash')")
    tt_multitab = driver.execute_script(
        "return window.localStorage.getItem('tt-multitab')"
    )
    tt_active_tab = driver.execute_script(
        "return window.localStorage.getItem('tt-active-tab')"
    )
    dc4_hash = driver.execute_script("return window.localStorage.getItem('dc4_hash')")

    localStorage = {
        "GramJs:apiCache": GramJs_apiCache,
        "dc2_hash": dc2_hash,
        "user_auth": user_auth,
        "dc": dc,
        "dc5_hash": dc5_hash,
        "dc4_auth_key": dc4_auth_key,
        "dc2_auth_key": dc2_auth_key,
        "dc5_auth_key": dc5_auth_key,
        "tgme_sync": tgme_sync,
        "kz_version": kz_version,
        "dc1_auth_key": dc1_auth_key,
        "tt-global-state": tt_global_state,
        "dc1_hash": dc1_hash,
        "tt-multitab": tt_multitab,
        "tt-active-tab": tt_active_tab,
        "dc4_hash": dc4_hash,
    }

    with open(storagePath, "w") as f:
        yaml.safe_dump(localStorage, f)

    driver.close()


def run(url):
    localStorage = yaml.safe_load(open(storagePath))
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
    driver.get(url)
    for key, value in localStorage.items():
        js_code = f"localStorage.setItem('{key}', '{value.replace("'", r"\'")}');"
        driver.execute_script(js_code)
    time.sleep(20000)
    driver.close()

def printStorage():
    localStorage = yaml.safe_load(open(storagePath))
    
    print(localStorage["tt-global-state"])


if __name__ == "__main__":
    global data
    with open(configPath, "rb") as f:
        data = list(yaml.safe_load_all(f))[0]

    url = data["url"]

    # getStorage(url)

    # run(url)
    
    printStorage()
