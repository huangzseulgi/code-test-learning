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

# 把浏览器最大化
driver.maximize_window()

driver.get("https://jd.com")
guide = driver.find_element(by=By.CSS_SELECTOR, value="#shortcutSitenavButton")
# 完成鼠标悬停
from selenium.webdriver.common.action_chains import ActionChains
import time

ActionChains(driver).move_to_element(guide).perform()
time.sleep(2)
#
jdjr = driver.find_element(by=By.CSS_SELECTOR, value="#ttbar-navs > div.dd.dropdown-layer > dl.fore1 > dd > div:nth-child(1) > a")
jdjr.click()




