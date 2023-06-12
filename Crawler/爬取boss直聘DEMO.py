# 导入selenium库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

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


# 打开目标网页
driver.get("https://www.zhipin.com/")
wait = WebDriverWait(driver, 10)

# 定位搜索框元素，输入关键词
element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'query')]")))
search_box = driver.find_element(By.XPATH, "//input[contains(@name,'query')]")
search_box.send_keys("运维工程师")

# 定位搜索按钮元素，点击搜索
search_button = driver.find_element(By.XPATH, "//button[contains(@class,'btn-search')]")
ActionChains(driver).move_to_element(search_button).click().perform()

time.sleep(5)

# 获取当前页面的所有职位元素
jobs = driver.find_elements(By.XPATH, "//ul[contains(@class,'job-list-box')]")

for item in jobs:
    job_titles = item.find_elements(By.XPATH, "//div[@class='job-card-body clearfix']/a[@class='job-card-left']")
    print(job_titles[0].text)
    print(job_titles[0].get_attribute('href'))
    company_titles = item.find_elements(By.XPATH, "//div[@class='job-card-body clearfix']/div[@class='job-card-right']")
    print(company_titles[0].text)
    company_urls = item.find_elements(By.XPATH, "//div[@class='job-card-body clearfix']/div[@class='job-card-right']/div[@class='company-info']/h3[@class='company-name']/a")
    print(company_urls[0].get_attribute('href'))



# print(type(jobs))
# print(jobs)

# 遍历每个职位元素，获取数据并打印
# for job in jobs:
#     # 获取职位名称
#     title = job.find_element_by_class_name("job-title").text
#     # 获取薪资范围
#     salary = job.find_element_by_class_name("red").text
#     # 获取公司名称
#     company = job.find_element_by_class_name("company-text").find_element_by_tag_name("a").text
#     # 打印数据
#     print(title, salary, company)

# 关闭浏览器
driver.quit()