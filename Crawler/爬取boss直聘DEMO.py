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
JOB_KEY = quote("运维工程师")
url = f"https://www.zhipin.com/web/geek/job?query={JOB_KEY}&city=101190400"
driver.get(url)

wait = WebDriverWait(driver, 60)
# 定位搜索框元素，输入关键词
# element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'query')]")))
# search_box = driver.find_element(By.XPATH, "//input[contains(@name,'query')]")
# search_box.send_keys("运维工程师")

# 定位搜索按钮元素，点击搜索
# search_button = driver.find_element(By.XPATH, "//button[contains(@class,'btn-search')]")
# ActionChains(driver).move_to_element(search_button).click().perform()
info = []
while True:
    # 获取当前页面的所有职位元素
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class,'job-list-box')]")))
    jobs = driver.find_elements(By.XPATH, "//ul[contains(@class,'job-list-box')]")

    for item in jobs:
        element = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='job-card-body clearfix']/a[@class='job-card-left']")))
        job_titles = item.find_elements(By.XPATH, "//div[@class='job-card-body clearfix']/a[@class='job-card-left']")
        # print(job_titles[0].text)
        # print(job_titles[0].get_attribute('href'))
        company_titles = item.find_elements(By.XPATH,
                                            "//div[@class='job-card-body clearfix']/div[@class='job-card-right']")
        # print(company_titles[0].text)
        company_urls = item.find_elements(By.XPATH,
                                          "//div[@class='job-card-body clearfix']/div[@class='job-card-right']/div[@class='company-info']/h3[@class='company-name']/a")
        # print(company_urls[0].get_attribute('href'))

    info.extend([[job_titles[i].text, job_titles[i].get_attribute('href'), company_titles[0].text,
                  company_urls[0].get_attribute('href')] for i in range(len(job_titles))])
    # print(len(info))

    if (len(driver.find_elements(By.XPATH,
                                 "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[contains(text(), '...')]")) == 1):
        end_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[10]")))
        if 'disabled' in end_button.get_attribute('class'):
            break
        else:
            try:
                end_button.click()
            except StaleElementReferenceException:
                end_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                        "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[10]")))
                end_button.click()
    else:
        end_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[11]")))
        try:
            end_button.click()
        except StaleElementReferenceException:
            end_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                    "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[11]")))
            end_button.click()
    time.sleep(6)

print(len(info))
for item in info:
    print(item)

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