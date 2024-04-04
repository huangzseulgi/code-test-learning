# web自动化测试只测试对的 主要的脉络
import time

import pytest
from selenium.webdriver.common.by import By
from const import URL, USERNAME, PASSWORD
from utils.webtest_utils import to_new_handle


@pytest.mark.skip
def test_login_success(get_webdriver):
    driver = get_webdriver
    # 进入页面慕慕生鲜
    driver.get(URL)
    # 窗口最大化
    # 注意:在不把窗口最大化之前，页面中并没有加载出“请登录”的按键因此找不到
    driver.maximize_window()
    # 点击请登录
    driver.find_element(by=By.LINK_TEXT, value="请登录").click()
    # # 获取当前句柄
    # login_page_handle = driver.current_window_handle
    username = driver.find_element(by=By.CSS_SELECTOR, value="[type=text]")
    password = driver.find_element(by=By.CSS_SELECTOR, value="[type=password]")
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    # 点击立即登录
    login_button = driver.find_element(by=By.CSS_SELECTOR, value="[type=button]")
    login_button.click()
    time.sleep(3)

    # 应该如何做断言来判断
    """
        login的断言方案：判断网址是否正确
    """
    assert driver.current_url == URL
    driver.close()
    time.sleep(3)
    driver.quit()
"""
    购物车的断言方案
        方法1. 清空购物车(连接数据库-选择用户将其数据清除
        方法2. 在做测试之前，记录购物车中有什么，添加购物车之后，再判断是否正确
"""
