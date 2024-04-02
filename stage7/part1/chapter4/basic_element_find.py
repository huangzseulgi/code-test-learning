# 使用ID进行定位
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_testing_path = r"E:\chrome-win64\chrome.exe"
chromedriver = r"E:\chromedriver-win64\chromedriver.exe"

# option
option = webdriver.ChromeOptions()
option.binary_location = chrome_testing_path
option.add_experimental_option("detach", True)
# 隐藏正在收到自动测试软件的控制这句话
option.add_experimental_option('excludeSwitches',
                               ['enable-automation'])

# service
service = Service(chromedriver)

# 驱动
driver = webdriver.Chrome(service=service, options=option)
driver.get("https://www.baidu.com")
"""
    ID定位
"""
# input_element = driver.find_element(by="id", value="kw")
# input_element.send_keys("大周老师")
# search_button = driver.find_element(by="id", value="su")
# search_button.click()

input_element = driver.find_element(by=By.ID, value="kw")
input_element.send_keys("大周老师")
search_button = driver.find_element(by=By.ID, value="su")
search_button.click()

