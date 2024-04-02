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
driver.get("https://www.jd.com")
"""
    class定位
"""
# 把浏览器最大化
driver.maximize_window()

driver.get("https://jd.com")
driver.find_element(by=By.CSS_SELECTOR, value="#key").send_keys("键盘")
# id为search的孩子div的类form的孩子button
driver.find_element(by=By.CSS_SELECTOR, value="#search > div > div.form > button > i").click()



