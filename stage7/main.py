# 驱动浏览器并打开百度网址

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_testing = r"E:\chrome-win64\chrome.exe"
chromedriver = r"E:\chromedriver-win64\chromedriver.exe"

option = webdriver.ChromeOptions()
option.binary_location = chrome_testing
option.add_experimental_option("detach", True)

service = Service(chromedriver)

driver = webdriver.Chrome(service=service, options=option)



