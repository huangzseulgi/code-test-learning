from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_testing_path = r"E:\chrome-win64\chrome.exe"
chromedriver = r"E:\chromedriver-win64\chromedriver.exe"

options = webdriver.ChromeOptions()
options.binary_location = chrome_testing_path
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches',
                                ['enable-automation'])

service = Service(chromedriver)

driver = webdriver.Chrome(options=options, service=service)

handlers = driver.window_handles  # 获取所有句柄
for h in handlers:
    if h != driver.current_window_handle:
        driver.switch_to.window(h)

driver.get("https://baidu.com")
driver.find_element(by=By.NAME, value="wd").send_keys("大周老师")
driver.find_element(by=By.ID, value="su").click()
# 链接的模糊搜索
handlers = driver.window_handles  # 获取所有句柄

for h in handlers:
    if h != driver.current_window_handle:
        driver.switch_to.window(h)
    print("当前句柄是：" + driver.title)

