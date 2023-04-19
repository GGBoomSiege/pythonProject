from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time

# 自动打开浏览器并且最大化窗口
driver = webdriver.Chrome()
driver.maximize_window()

# 自动输入淘宝网址，并根据链接文本选择元素，点击界面上的登录按钮
driver.get('https://www.taobao.com')
if driver.find_element(By.LINK_TEXT, '亲，请登录'):
    driver.find_element(By.LINK_TEXT, '亲，请登录').click()
    print("请在15秒内完成扫码")
    time.sleep(15)
    # 打开购物车列表首页
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(2)
# 点击全选按钮
if driver.find_element(By.ID, 'J_SelectAll1'):
    driver.find_element(By.ID, 'J_SelectAll1').click()

now = datetime.datetime.now()
print("login success:", now.strftime("%Y-%m-%d %H:%M:%S"))


def buy(times):
    while True:
        # 记录当前时间，使用datatime内置模块
        now2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(times)
        print(now2)
        # 对比时间，时间到的话就点击结算
        if now2 >= times:
            try:
                if driver.find_element(By.ID, 'J_Go'):
                    driver.find_element(By.ID, 'J_Go').click()
                    driver.find_element(By.LINK_TEXT, '提交订单').click()
                    print('抢购成功，请尽快付款')
            except:
                print('请再次尝试提交订单')
        # print(now2)
        time.sleep(0.1)


if __name__ == "__main__":
    buy_times = input("请输入抢购时间(例如格式：2022-08-17 21:00:00):")
    buy(buy_times)