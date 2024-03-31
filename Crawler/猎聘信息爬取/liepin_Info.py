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
import random

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
                        "//div[@class='job-list-box']/div/div[@class='jsx-2297469327 job-card-pc-container']",
                    )
                )
            )
            jobs_title = driver.find_elements(
                By.XPATH, "//div[@class='jsx-2693574896 ellipsis-1']"
            )
            jobs_location = driver.find_elements(
                By.XPATH, "//span[@class='jsx-2693574896 ellipsis-1']"
            )
            salary = driver.find_elements(
                By.XPATH, "//span[@class='jsx-2693574896 job-salary']"
            )
            # jobs_url = driver.find_elements(By.XPATH, "//a[@class='jsx-2693574896']")
            jobs_url = driver.find_elements(By.XPATH, "//a[@class='jsx-2693574896 ']")
            company_titles = driver.find_elements(
                By.XPATH, "//span[@class='jsx-2693574896 company-name ellipsis-1']"
            )
            company_size = driver.find_elements(
                By.XPATH, "//div[@class='jsx-2693574896 company-tags-box ellipsis-1']"
            )

            # print(flag)
            # print(len(jobs_url))

            for num in range(len(jobs_title)):
                infos.extend(
                    [
                        {
                            "job_title": jobs_title[num].text,
                            "job_location": jobs_location[num].text,
                            "salary": salary[num].text,
                            "job_url": jobs_url[num].get_attribute("href"),
                            "company_title": company_titles[num].text,
                            "company_size": company_size[num].text,
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
            print(driver.current_url)
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
        CITY_KEY = "060080"  # 苏州
        # CITY_KEY = '060100' # 无锡
    except Exception as e:
        print("您的输入有误，请重新输入。")
    # jobs = clean_data(get_jobs(JOB_KEY, CITY_KEY))
    jobs = get_jobs(JOB_KEY, CITY_KEY)
    run_database(jobs)
