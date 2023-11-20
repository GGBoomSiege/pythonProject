# 导入selenium库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from itertools import zip_longest
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import datetime
import uuid
import time

url = ''


def unique_lease_id():
    unique_lease_id_lst = [datetime.datetime.now().strftime('%Y%m%d'), str(uuid.uuid4().int % (10 ** 8))]
    unique_lease_id = int(''.join(unique_lease_id_lst))
    return unique_lease_id


def get_jobs(JOB_KEY,CITY_KEY):
    # 创建一个webdriver对象，指定浏览器类型和驱动程序路径
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument('--ignore-certificate-errors')
    service = webdriver.chrome.service.Service(executable_path=r"E:\Python\Python312\chromedriver.exe")
    service_log_path = 'chromedriver.log'
    service.service_log_path = service_log_path
    driver = webdriver.Chrome(options=options, service=service)
    driver.set_window_size(1920, 1080)
    driver.minimize_window()

    # 打开目标网页
    url = f"https://www.zhipin.com/web/geek/job?query={quote(JOB_KEY)}&city={CITY_KEY}"
    driver.get(url)
    print(url)

    wait = WebDriverWait(driver, 60)
    # 定位搜索框元素，输入关键词
    # element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'query')]")))
    # search_box = driver.find_element(By.XPATH, "//input[contains(@name,'query')]")
    # search_box.send_keys("运维工程师")

    # 定位搜索按钮元素，点击搜索
    # search_button = driver.find_element(By.XPATH, "//button[contains(@class,'btn-search')]")
    # ActionChains(driver).move_to_element(search_button).click().perform()
    infos = []
    while True:
        try:
            # 获取当前页面的所有职位元素
            element = wait.until(
                EC.presence_of_element_located((By.XPATH, "//ul[contains(@class,'job-list-box')]")))
            jobs = driver.find_elements(By.XPATH, "//ul[contains(@class,'job-list-box')]")
            for item in jobs:
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='job-card-body clearfix']/a[@class='job-card-left']")))
                job_titles = item.find_elements(By.XPATH,
                                                "//div[@class='job-card-body clearfix']/a[@class='job-card-left']")
                # print(job_titles[0].text)
                # print(job_titles[0].get_attribute('href'))
                company_titles = item.find_elements(By.XPATH,
                                                    "//div[@class='job-card-body clearfix']/div[@class='job-card-right']")
                # print(company_titles[0].text)
                company_urls = item.find_elements(By.XPATH,
                                                  "//div[@class='job-card-body clearfix']/div[@class='job-card-right']/div[@class='company-info']/h3[@class='company-name']/a")
                # print(company_urls[0].get_attribute('href'))

            flag = 0

            for i in range(len(job_titles)):
                if job_titles[i].text.find('猎头') != -1:
                    infos.extend([
                        [
                            job_titles[i].text,
                            job_titles[i].get_attribute('href'),
                            '',
                            ''
                        ]
                    ])
                else:
                    infos.extend([
                        [
                            job_titles[i].text,
                            job_titles[i].get_attribute('href'),
                            company_titles[flag].text,
                            company_urls[flag].get_attribute('href')
                        ]
                    ])
                    flag += 1

            if (len(driver.find_elements(By.XPATH,
                                         "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[contains(text(), '...')]")) == 1):
                end_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                        "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[10]")))
                if 'disabled' in end_button.get_attribute('class'):
                    break
                else:
                    try:
                        url = driver.current_url
                        end_button.click()
                    except StaleElementReferenceException:
                        end_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                                "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[10]")))
                        url = driver.current_url
                        end_button.click()
            else:
                end_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                        "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[11]")))
                try:
                    url = driver.current_url
                    end_button.click()
                except StaleElementReferenceException:
                    end_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                            "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[11]")))
                    url = driver.current_url
                    end_button.click()
            print(url)
        except Exception as e:
            continue

    # 关闭浏览器
    driver.quit()
    return infos


def clean_data(data):
    '''
    {
        "job_info" : {
            "job_title": "运维工程师",
            "location": "北京",
            "salary": "面议",
            "experience": "1-3年",
            "education": "本科",
            "hr": "王女士",
            "status": "在线",
        },
        "job_url": "https://www.zhipin.com/job/101190400-101190500/?query=运维工程师&city=101190400",
        "company_info" : {
            "organization_name": "马太科技",
            "organization_size":"互联网不需要融资100-499人"
        },
        "company_url": "https://www.zhipin.com/company/101190400-101190500/"
    }
    '''
    job_info_lst = ["job_title", "location", "salary", "experience", "education", "hr", "status"]
    job_url_lst = ["job_url"]
    company_info_lst = ["organization_name", "organization_size"]
    company_url_lst = ["company_url"]
    job_info = {}
    job_url = {}
    company_info = {}
    company_url = {}
    clear_data = []
    for item in range(len(data)):
        if company_info == '' and company_url == '':
            job_info = {key: value for key, value in zip_longest(job_info_lst, data[item][0].split('\n'), fillvalue="")}
            job_url = {key: value for key, value in zip_longest(job_url_lst, [data[item][1]], fillvalue="")}
            company_info = {
                "organization_name": "",
                "organization_size": ""
            }
            company_url = {
                "company_url": ""
            }
        else:
            job_info = {key: value for key, value in zip_longest(job_info_lst, data[item][0].split('\n'), fillvalue="")}
            job_url = {key: value for key, value in zip_longest(job_url_lst, [data[item][1]], fillvalue="")}
            company_info = {key: value for key, value in
                            zip_longest(company_info_lst, data[item][2].split('\n'), fillvalue="")}
            company_url = {key: value for key, value in zip_longest(company_url_lst, [data[item][3]], fillvalue="")}
        clear_data.append([job_info, job_url, company_info, company_url])
    return clear_data


def run_database(data):
    # 创建连接引擎
    engine = create_engine('mysql+pymysql://root:operator_123456@127.0.0.1/job_info')

    # 创建会话工厂
    Session = sessionmaker(bind=engine)
    session = Session()

    # 创建映射类
    Base = declarative_base()

    class JobInfomation(Base):
        __tablename__ = 'job_infomation'
        id = Column(BigInteger, primary_key=True, default=unique_lease_id)
        job_title = Column(String(64))
        location = Column(String(64))
        salary = Column(String(64))
        experience = Column(String(64))
        education = Column(String(64))
        hr = Column(String(64))
        status = Column(String(64))
        job_url = Column(Text(65535))
        organization_name = Column(String(64))
        organization_size = Column(String(64))
        company_url = Column(Text(65535))

    Base.metadata.create_all(engine)
    session.query(JobInfomation).delete()

    # 创建对象并插入数据
    for item in data:
        obj = JobInfomation(
            job_title=item[0]['job_title'],
            location=item[0]['location'],
            salary=item[0]['salary'],
            experience=item[0]['experience'],
            education=item[0]['education'],
            hr=item[0]['hr'],
            status=item[0]['status'],
            job_url=item[1]['job_url'],
            organization_name=item[2]['organization_name'],
            organization_size=item[2]['organization_size'],
            company_url=item[3]['company_url']
        )
        session.add(obj)

    session.commit()
    # 关闭会话
    session.close()

def get_database():
    # 创建连接引擎
    engine = create_engine('mysql+pymysql://root:operator_123456@192.168.3.234/job_info')

    # 创建会话工厂
    Session = sessionmaker(bind=engine)
    session = Session()

    # 创建映射类
    Base = declarative_base()

    class JobInfomation(Base):
        __tablename__ = 'job_infomation'
        id = Column(BigInteger, primary_key=True, default=unique_lease_id)
        job_title = Column(String(64))
        location = Column(String(64))
        salary = Column(String(64))
        experience = Column(String(64))
        education = Column(String(64))
        hr = Column(String(64))
        status = Column(String(64))
        job_url = Column(Text(65535))
        organization_name = Column(String(64))
        organization_size = Column(String(64))
        company_url = Column(Text(65535))

    Base.metadata.create_all(engine)
    session.query(JobInfomation).delete()

    # 创建对象并插入数据
    for item in data:
        obj = JobInfomation(
            job_title=item[0]['job_title'],
            location=item[0]['location'],
            salary=item[0]['salary'],
            experience=item[0]['experience'],
            education=item[0]['education'],
            hr=item[0]['hr'],
            status=item[0]['status'],
            job_url=item[1]['job_url'],
            organization_name=item[2]['organization_name'],
            organization_size=item[2]['organization_size'],
            company_url=item[3]['company_url']
        )
        session.add(obj)

    session.commit()
    # 关闭会话
    session.close()

if __name__ == '__main__':
    try:
        # JOB_KEY = input('请输入需要查询的岗位名称:')
        JOB_KEY = '运维'
        CITY_KEY = '101190400' # 苏州
        # CITY_KEY = '101190200' # 无锡
    except Exception as e:
        print("您的输入有误，请重新输入。")
    jobs = clean_data(get_jobs(JOB_KEY, CITY_KEY))
    run_database(jobs)
    # for item in jobs:
    #     print(
    #         item[0]['job_title'], item[0]['location'], item[0]['salary'], item[0]['experience'], item[0]['education'], item[0]['hr'], item[0]['status'],
    #         item[1]['job_url'], item[2]['organization_name'], item[2]['organization_size'],
    #         item[3]['company_url']
    #     )
