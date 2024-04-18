from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import yaml
import time

configPath = "./Crawler/猎聘信息爬取/liepin_info.yaml"


def shoucang_jobs(urls):
    # 创建一个webdriver对象，指定浏览器类型和驱动程序路径
    options = webdriver.ChromeOptions()

    options.add_experimental_option("debuggerAddress", "127.0.0.1:9922")
    driver = webdriver.Chrome(options=options)

    # 打开目标网页
    for i in range(len(urls)):
        try:
            print(i)
            driver.get(urls[i])
            wait = WebDriverWait(driver, 4)
            # 获取当前页面的所有职位元素
            shoucang_btn = wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        # "/html/body/section[@class='job-apply-container']/div[@class='job-apply-operate']/div[@class='other-box']/a[contains(@class,'favor-box')]/span",
                        "/html/body/section[@class='job-apply-container']/div[@class='job-apply-operate']/div[@class='other-box']/a[@class='favor-box']/span",
                    )
                )
            )
            shoucang_btn.click()
            time.sleep(1)

        except Exception as e:
            continue


if __name__ == "__main__":
    global urls
    with open(configPath, "rb") as f:
        urls = yaml.load(f, Loader=yaml.FullLoader)

    shoucang_jobs(urls)
