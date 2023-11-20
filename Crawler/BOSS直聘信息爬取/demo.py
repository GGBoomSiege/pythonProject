from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep

if __name__ == '__main__':
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

    urls = []
    for n in range(1, 10):
        urls.append(
            f'https://www.zhipin.com/web/geek/job?query=%E8%BF%90%E7%BB%B4&city=101190400&page={n}')

    sleep(1)

    # for url in urls:
    #     driver.get(url)
    #     sleep(3)
    driver.get(urls[0])
    sleep(1)
    wait = WebDriverWait(driver, 60)
    end_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='pagination-area']/div[@class='pager text-center']/div[@class='options-pages']/a[10]")))
    end_button.click()
    sleep(1)
