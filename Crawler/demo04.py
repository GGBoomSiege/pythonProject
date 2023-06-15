# 导入selenium库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time

# 创建一个webdriver对象，指定浏览器类型和驱动程序路径
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# options = webdriver.ChromeOptions()
service = webdriver.chrome.service.Service(executable_path=r"D:\Python-3.11\chromedriver.exe")
service_log_path = 'chromedriver.log'
service.service_log_path = service_log_path
driver = webdriver.Chrome(options=options, service=service)
driver.minimize_window()

# 打开目标网页
JOB_KEY= "java"
url = f"https://www.zhipin.com/web/geek/job?query={quote(JOB_KEY)}&city=101190400"
driver.get(url)

wait = WebDriverWait(driver, 60)
# 定位搜索框元素，输入关键词
# element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'query')]")))
# search_box = driver.find_element(By.XPATH, "//input[contains(@name,'query')]")
# search_box.send_keys("运维工程师")

while True:
    try:
        # 获取当前页面的所有职位元素
        element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//ul[contains(@class,'job-list-box')]")))
        driver.find_elements(By.XPATH, "//ul[contains(@class,'job-list-box')]")
    except Exception as e:
        continue
    try:
        if r"https://www.zhipin.com/web/geek/job" in driver.current_url:
            driver.refresh()
            time.sleep(1)
            driver.find_elements(By.XPATH, "//ul[contains(@class,'job-list-box')]")
        else:
            continue
        break
    except Exception as e:
        continue
# 获取当前页面的所有职位元素
element = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class,'job-list-box')]")))
jobs = driver.find_elements(By.XPATH, "//ul[contains(@class,'job-list-box')]")
print(jobs)