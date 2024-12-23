# 导入selenium库
from bs4 import BeautifulSoup
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
import random
import re

url = ""


def unique_lease_id():
    unique_lease_id_lst = [
        datetime.datetime.now().strftime("%Y%m%d"),
        str(uuid.uuid4().int % (10**8)),
    ]
    unique_lease_id = int("".join(unique_lease_id_lst))
    return unique_lease_id


def get_jobs(JOB_KEY, CITY_KEY):
    # 创建一个webdriver对象，指定浏览器类型和驱动程序路径
    options = webdriver.ChromeOptions()

    options.add_experimental_option("debuggerAddress", "127.0.0.1:9922")
    driver = webdriver.Chrome(options=options)

    # 打开目标网页
    url = f"https://www.liepin.com/zhaopin/?city={CITY_KEY}&dq={CITY_KEY}&pubTime=&currentPage=0&pageSize=40&key={quote(JOB_KEY)}&suggestTag=&workYearCode=0&compId=&compName=&compTag=&industry=&salary=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&ckId=73xe2opyoxbwi79rfqd969yc3v7mpib9&scene=page&skId=wg8jxx7juvm5iuk5pfrav4sas0fepoub&fkId=wg8jxx7juvm5iuk5pfrav4sas0fepoub&sfrom=search_job_pc&suggestId="
    driver.get(url)
    # print(url)

    wait = WebDriverWait(driver, 60)

    infos = []

    while True:
        try:
            # 获取当前页面的所有职位元素
            wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div[@id='lp-search-job-box']/div[@class='content-wrap']/section[@class='content-left-section']/div[@class='job-list-box']/div/div[@class='jsx-2297469327 job-card-pc-container']",
                    )
                )
            )

            job_description = driver.find_elements(
                By.XPATH,
                "/html/body/div[@id='lp-search-job-box']/div[@class='content-wrap']/section[@class='content-left-section']/div[@class='job-list-box']/div/div[@class='jsx-2297469327 job-card-pc-container']",
            )

            for num in range(len(job_description)):
                company_title = (
                    BeautifulSoup(job_description[num].get_attribute("outerHTML"))
                    .find("span", class_=re.compile("jsx-.*company-name ellipsis-1"))
                    .text
                )
                if re.match(r"^某", company_title):
                    continue
                job_title = (
                    BeautifulSoup(job_description[num].get_attribute("outerHTML"))
                    .find("div", class_=re.compile("jsx-.*ellipsis-1"))
                    .text
                )
                job_location = (
                    BeautifulSoup(job_description[num].get_attribute("outerHTML"))
                    .find("span", class_=re.compile("jsx-.*ellipsis-1"))
                    .text
                )
                salary = (
                    BeautifulSoup(job_description[num].get_attribute("outerHTML"))
                    .find("span", class_=re.compile("jsx-.*job-salary"))
                    .text
                )
                job_url = (
                    BeautifulSoup(job_description[num].get_attribute("outerHTML"))
                    .find("a", class_=re.compile("jsx-.*"))
                    .get("href")
                )
                company_size = (
                    BeautifulSoup(job_description[num].get_attribute("outerHTML"))
                    .find(
                        "div", class_=re.compile("jsx-.*company-tags-box.*ellipsis-1")
                    )
                    .text
                )

                infos.extend(
                    [
                        {
                            "job_title": job_title,
                            "job_location": job_location,
                            "salary": salary,
                            "job_url": job_url,
                            "company_title": company_title,
                            "company_size": company_size,
                        }
                    ]
                )

            end_button = wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//li[contains(@class,'ant-pagination-next')]",
                    )
                )
            )

            if "disabled" in end_button.get_attribute("class"):
                break
            else:
                time.sleep(random.randint(1, 4))
                end_button.click()
        except Exception as e:
            print(e)
            continue

    # 关闭浏览器
    driver.quit()
    return infos


def run_database(data):
    # 创建连接引擎
    engine = create_engine("mysql+pymysql://root:operator_123456@127.0.0.1/liepin_info")

    # 创建会话工厂
    Session = sessionmaker(bind=engine)
    session = Session()

    # 创建映射类
    Base = declarative_base()

    class JobInfomation(Base):
        __tablename__ = "job_infomation"
        id = Column(BigInteger, primary_key=True, default=unique_lease_id)
        job_title = Column(String(64))
        location = Column(String(64))
        salary = Column(String(64))
        job_url = Column(Text(65535))
        organization_name = Column(String(64))
        organization_size = Column(String(64))

    Base.metadata.create_all(engine)
    session.query(JobInfomation).delete()

    # 创建对象并插入数据
    for item in data:
        obj = JobInfomation(
            job_title=item["job_title"],
            location=item["job_location"],
            salary=item["salary"],
            job_url=item["job_url"],
            organization_name=item["company_title"],
            organization_size=item["company_size"],
        )
        session.add(obj)

    session.commit()
    # 关闭会话
    session.close()


def get_database():
    # 创建连接引擎
    engine = create_engine(
        "mysql+pymysql://root:operator_123456@192.168.3.234/job_info"
    )

    # 创建会话工厂
    Session = sessionmaker(bind=engine)
    session = Session()

    # 创建映射类
    Base = declarative_base()

    class JobInfomation(Base):
        __tablename__ = "job_infomation"
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
            job_title=item[0]["job_title"],
            location=item[0]["location"],
            salary=item[0]["salary"],
            experience=item[0]["experience"],
            education=item[0]["education"],
            hr=item[0]["hr"],
            status=item[0]["status"],
            job_url=item[1]["job_url"],
            organization_name=item[2]["organization_name"],
            organization_size=item[2]["organization_size"],
            company_url=item[3]["company_url"],
        )
        session.add(obj)

    session.commit()
    # 关闭会话
    session.close()


if __name__ == "__main__":
    try:
        # JOB_KEY = input('请输入需要查询的岗位名称:')
        JOB_KEY = "运维"
        # JOB_KEY = "嵌入式"
        # JOB_KEY = "UX"
        # CITY_KEY = "020"  # 上海
        CITY_KEY = "060080"  # 苏州
        # CITY_KEY = '060100' # 无锡
        # CITY_KEY = "060020"  # 南京
    except Exception as e:
        print("您的输入有误，请重新输入。")
    # jobs = clean_data(get_jobs(JOB_KEY, CITY_KEY))
    jobs = get_jobs(JOB_KEY, CITY_KEY)
    run_database(jobs)
