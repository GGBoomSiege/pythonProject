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


def get_jobs(url):
    # 创建一个webdriver对象，指定浏览器类型和驱动程序路径
    options = webdriver.ChromeOptions()

    options.add_experimental_option("debuggerAddress", "127.0.0.1:9922")
    driver = webdriver.Chrome(options=options)

    # 打开目标网页
    driver.get(url)
    # print(url)

    wait = WebDriverWait(driver, 60)

    infos = []

    # 获取当前页面的所有职位元素
    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='job-list-box']/div/div[@class='jsx-2297469327 job-card-pc-container']",
            )
        )
    )
    job_description = driver.find_elements(
        By.XPATH,
        "//div[@class='content-wrap']/section[@class='content-left-section']/div[@class='job-list-box']/div/div[@class='jsx-2297469327 job-card-pc-container']",
    )
    # jobs_title = job_description.find_elements(
    #     By.XPATH, "//div[@class='jsx-2693574896 ellipsis-1']"
    # )
    # jobs_title = driver.find_elements(
    #     By.XPATH, "//div[@class='jsx-2693574896 ellipsis-1']"
    # )
    # jobs_location = driver.find_elements(
    #     By.XPATH, "//span[@class='jsx-2693574896 ellipsis-1']"
    # )
    # salary = driver.find_elements(
    #     By.XPATH, "//span[@class='jsx-2693574896 job-salary']"
    # )
    # # jobs_url = driver.find_elements(By.XPATH, "//a[@class='jsx-2693574896']")
    # jobs_url = driver.find_elements(By.XPATH, "//a[@class='jsx-2693574896 ']")
    # company_titles = driver.find_elements(
    #     By.XPATH, "//span[@class='jsx-2693574896 company-name ellipsis-1']"
    # )
    # company_size = driver.find_elements(
    #     By.XPATH, "//div[@class='jsx-2693574896 company-tags-box ellipsis-1']"
    # )

    # print(flag)
    # print(len(jobs_url))

    # for num in range(len(company_size)):
    #     print(company_size[num].text)

    for num in range(len(job_description)):
        # infos.extend(
        #     [
        #         {
        #             "job_title": jobs_title[num].text,
        #             "job_location": jobs_location[num].text,
        #             "salary": salary[num].text,
        #             "job_url": jobs_url[num].get_attribute("href"),
        #             "company_title": company_titles[num].text,
        #             "company_size": company_size[num].text,
        #         }
        #     ]
        # )
        jobs_title = job_description[num].find_elements(
            By.XPATH, "//div[@class='jsx-2693574896 ellipsis-1']"
        )
        print(job_description[num].text)

    # 关闭浏览器
    driver.quit()
    return infos


if __name__ == "__main__":
    get_jobs(
        "https://www.liepin.com/zhaopin/?city=060080&dq=060080&pubTime=&currentPage=7&pageSize=40&key=%E7%94%9F%E7%89%A9&suggestTag=&workYearCode=0&compId=&compName=&compTag=&industry=&salary=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&sfrom=search_job_pc&ckId=g9bdzp11yfxbtiq4u6aexz5bevaifi9b&skId=wg8jxx7juvm5iuk5pfrav4sas0fepoub&fkId=wg8jxx7juvm5iuk5pfrav4sas0fepoub&scene=page&suggestId="
    )
