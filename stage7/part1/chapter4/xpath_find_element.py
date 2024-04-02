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
# 把浏览器最大化
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id=\"key\"]").send_keys("电脑")
driver.find_element(By.XPATH, "//*[@id=\"search\"]/div/div[2]/button").click()

