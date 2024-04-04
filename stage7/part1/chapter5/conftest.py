import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from const import CHROME_PATH, DRIVER_PATH


# 在每一次会话中会执行获取一次driver 就不会重复打开浏览器了
@pytest.fixture(scope="session")
def get_webdriver():
    options = webdriver.ChromeOptions()
    options.binary_location = CHROME_PATH
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches',
                                    ['enable-automation'])
    print(DRIVER_PATH)
    service = Service(DRIVER_PATH)

    driver = webdriver.Chrome(options=options, service=service)
    return driver
