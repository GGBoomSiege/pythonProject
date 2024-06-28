# 导入selenium库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from selenium.common.exceptions import StaleElementReferenceException
import re
from itertools import zip_longest
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import datetime
import uuid
from decimal import Decimal
import time


def unique_lease_id():
    unique_lease_id_lst = [
        datetime.datetime.now().strftime("%Y%m%d"),
        str(uuid.uuid4().int % (10**8)),
    ]
    unique_lease_id = int("".join(unique_lease_id_lst))
    return unique_lease_id


def get_leases(url):
    # 创建一个webdriver对象，指定浏览器类型和驱动程序路径
    options = webdriver.ChromeOptions()

    options.add_experimental_option("debuggerAddress", "127.0.0.1:9922")
    driver = webdriver.Chrome(options=options)
    # # 创建一个webdriver对象，指定浏览器类型和驱动程序路径
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # # options = webdriver.ChromeOptions()
    # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    # options.add_argument(f"user-agent={user_agent}")
    # service = webdriver.chrome.service.Service(executable_path=r"D:\Python-3.11\chromedriver.exe")
    # service_log_path = 'chromedriver.log'
    # service.service_log_path = service_log_path
    # driver = webdriver.Chrome(options=options, service=service)
    # driver.set_window_size(1920, 1080)
    # driver.minimize_window()

    # 打开目标网页
    driver.get(url)

    wait = WebDriverWait(driver, 60)

    infos = []
    while True:
        try:
            # 获取当前页面的所有职位元素
            element = wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//div[@class='lfBox lf']/div[@class='list-con-box']/ul[@class='pList rentList']",
                    )
                )
            )

            leases_info = driver.find_elements(
                By.XPATH,
                "//div[@class='lfBox lf']/div[@class='list-con-box']/ul[@class='pList rentList']",
            )

            leases_title = leases_info[0].find_elements(
                By.XPATH, "//div[@class='listCon']/h3[@class='listTit']/a"
            )
            leases_size = leases_info[0].find_elements(
                By.XPATH, "//div[@class='listCon']/div[@class='listX']/p[1]"
            )
            leases_location = leases_info[0].find_elements(
                By.XPATH, "//div[@class='listCon']/div[@class='listX']/p[2]"
            )
            leases_status = leases_info[0].find_elements(
                By.XPATH, "//div[@class='listCon']/div[@class='listX']/p[3]"
            )
            leases_salary = leases_info[0].find_elements(
                By.XPATH, "//div[@class='listX']/div[@class='jia']/p[@class='redC']"
            )
            leases_type = leases_info[0].find_elements(
                By.XPATH,
                "//div[@class='listCon']/div[@class='listX']/div[@class='jia']/p[2]",
            )

            # for item in leases_title:
            #     print(item.text)

            infos.extend(
                [
                    [
                        re.sub(r"\s+", "", leases_title[i].text),
                        re.sub(r"\s+", "", leases_title[i].get_attribute("href")),
                        re.sub(r"\s+", "", leases_size[i].text).split("·")[0],
                        "·".join(
                            re.sub(r"\s+", "", leases_size[i].text).split("·")[1:]
                        ),
                        leases_location[i].text.split(" ")[0],
                        re.sub(
                            r"\s+", "", "".join(leases_location[i].text.split(" ")[1:])
                        ),
                        re.sub(r"\s+", "", leases_salary[i].text).split("元")[0],
                        re.sub(r"\s+", "", leases_type[i].text),
                    ]
                    for i in range(len(leases_title))
                ]
            )

            flag = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='lfBox lf']/div[@class='pageBox']")
                )
            )

            if "下一页" not in flag.text:
                break
            else:
                time.sleep(4)
                driver.find_element(
                    By.XPATH,
                    "//div[@class='lfBox lf']/div[@class='pageBox']/div[@class='pageSty rf']/a[@class='cPage'][1]",
                ).click()

        except Exception as e:
            print(e)
            continue

    # 关闭浏览器
    driver.quit()
    return infos


def clean_data(data):
    """
    {
        'home':'整租·狮山·天都花园·3室',
        'home_url':'https://sz.5i5j.com/zufang/45683545.html',
        'home_size':'3 室 2 厅',
        'home_size_more':'140㎡ · 南 · 中楼层/30层 · 精装',
        'home_location':'狮山',
        'home_more_location':'天都花园 · 距离地铁玉山路445米'
        'home_salary':'5500元/月',
        'lease_type':'出租方式：整租'
        ['整租·科技城·永新秀郡·3室', 'https://sz.5i5j.com/zufang/45682754.html', '3室2厅', '90㎡·南北·中楼层/18层·精装', '科技城', '永新秀郡', '3000', '出租方式：整租']
    }
    """
    data_head = [
        "home",
        "home_url",
        "home_size",
        "home_size_more",
        "home_location",
        "home_more_location",
        "home_salary",
        "lease_type",
    ]
    clean_data = []
    for item in data:
        data_dict = {
            key: value for key, value in zip_longest(data_head, item, fillvalue="")
        }
        clean_data.append(data_dict)
    return clean_data


def run_database(data):
    # 创建连接引擎
    engine = create_engine("mysql+pymysql://root:operator_123456@127.0.0.1/home_info")

    # 创建会话工厂
    Session = sessionmaker(bind=engine)
    session = Session()

    # 创建映射类
    Base = declarative_base()

    class HomeInfomation(Base):
        __tablename__ = "home_infomation"
        id = Column(BigInteger, primary_key=True, default=unique_lease_id)
        home = Column(String(64))
        home_url = Column(String(64))
        home_size = Column(String(64))
        home_size_more = Column(String(64))
        home_location = Column(String(64))
        home_more_location = Column(String(64))
        home_salary = Column(DECIMAL)
        lease_type = Column(String(64))

    Base.metadata.create_all(engine)
    session.query(HomeInfomation).delete()

    # 创建对象并插入数据
    for item in data:
        if item["home_salary"] == "":
            item["home_salary"] = "0"

        obj = HomeInfomation(
            home=item["home"],
            home_url=item["home_url"],
            home_size=item["home_size"],
            home_size_more=item["home_size_more"],
            home_location=item["home_location"],
            home_more_location=item["home_more_location"],
            home_salary=Decimal(item["home_salary"]),
            lease_type=item["lease_type"],
        )
        session.add(obj)

    session.commit()
    # 关闭会话
    session.close()


if __name__ == "__main__":
    url = f"https://sz.5i5j.com/zufang/"

    start_time = datetime.datetime.now()
    lease = get_leases(url)
    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    print(f"信息收集完成,共计耗时{time_diff.total_seconds()}秒,共{len(lease)}条数据。")

    # print(lease)

    start_time = datetime.datetime.now()
    data = clean_data(lease)
    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    print(f"数据清理完成,共计耗时{time_diff.total_seconds()}秒")

    # print(data)

    start_time = datetime.datetime.now()
    run_database(data)
    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    print(f"数据载入完成,共计耗时{time_diff.total_seconds()}秒")
