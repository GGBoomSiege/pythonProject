from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep

def get_jobs():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    service = webdriver.chrome.service.Service(
        executable_path=r"E:\Python\Python312\chromedriver.exe")
    service_log_path = 'chromedriver.log'
    service.service_log_path = service_log_path
    driver = webdriver.Chrome(options=options, service=service)
    driver.set_window_size(1920, 1080)
    # driver.minimize_window()

    # -我是最新谷歌浏览器版本，chrome在79和79版之后用这个，
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
    """
    })

    # urls = []
    # for n in range(1, 10):
    #     urls.append(
    #         f'https://www.zhipin.com/web/geek/job?query=%E8%BF%90%E7%BB%B4&city=101190400&page={n}')

    # sleep(1)

    # for url in urls:
    #     driver.get(url)
    #     sleep(3)

    url = "https://www.liepin.com/zhaopin/?city=060080&dq=060080&pubTime=&currentPage=0&pageSize=40&key=%E8%BF%90%E7%BB%B4"

    driver.get(url)
    # sleep(1)
    wait = WebDriverWait(driver, 10)

    passwordLoginBtn = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='jsx-251077603 aside-login-box']/div[@class='jsx-2597420583 login-container']/div[@class='jsx-3565815463 login-tabs']/div[@class='jsx-3565815463 login-tabs-line']/div[@class='jsx-3565815463 login-tabs-line-text']")))
    passwordLoginBtn.click()

    username = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='login']")))
    password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='pwd']")))
    checkBtn = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@class='ant-checkbox-wrapper']/span[@class='ant-checkbox']/input[@class='ant-checkbox-input']")))
    loginBtn = wait.until(EC.presence_of_element_located((By.XPATH, "//form[@class='ant-form ant-form-horizontal ant-form-large']/button[@class='ant-btn ant-btn-primary ant-btn-round ant-btn-lg login-submit-btn']/span")))

    username.send_keys("13140725066")
    password.send_keys("196153539LJlj!")
    checkBtn.click()
    loginBtn.click()

    sleep(5)

    end_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//li[@class='ant-pagination-next']/button[@class='ant-pagination-item-link']/span[@class='anticon anticon-right']")))
    while True:
        element = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='jsx-2297469327 job-card-pc-container']")))
        print(element.text)
        sleep(1)
        end_button.click()
        try:
            end_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//li[@class='ant-pagination-next']/button[@class='ant-pagination-item-link']/span[@class='anticon anticon-right']")))
        except Exception as e:
            break
    sleep(120)


if __name__ == '__main__':
    pass