# web自动化测试只测试对的 主要的脉络
import time
import pytest
from selenium.webdriver.common.by import By
from const import URL, USERNAME, PASSWORD
from utils.webtest_utils import to_new_handle

"""
    扫描二维码并登录 获取cookies
"""
@pytest.mark.skip
def test_login_success(get_webdriver):
    driver = get_webdriver
    # 进入页面慕慕生鲜
    driver.get("https://www.jd.com/")
    # 窗口最大化
    driver.maximize_window()
    # 点击请登录
    driver.find_element(by=By.CSS_SELECTOR, value="[class=link-login]").click()
    # 点击二维码登录
    driver.find_element(by=By.CSS_SELECTOR, value="#content > div.login-wrap > div.w > div > div > div.login-form-body > div.login-tab.login-tab-l > a").click()
    while True:
        print(driver.current_url)
        if driver.current_url == "https://www.jd.com/":
            break
        time.sleep(3)
    print("登录成功")
    cookies = driver.get_cookies()
    print(cookies)
    driver.find_element(by=By.LINK_TEXT, value="我的购物车").click()


"""
    用上面获取的cookies跳过登录
    点击到购物车 并将页面下滑到底端点击“售后服务”跳转到帮助中心
"""
# @pytest.mark.skip
def test_login_success_using_cookies(get_webdriver):
    # 将上一步的cookie复制粘贴在这里
    cookies = 1
    driver = get_webdriver
    # 进入页面慕慕生鲜
    driver.get("https://www.jd.com/")
    # 添加cookies
    for c in cookies:
        driver.add_cookie(c)

    # 窗口最大化
    driver.maximize_window()
    index_page_handle = driver.current_window_handle
    print(driver.current_url)
    time.sleep(3)
    # 点击进入购物车
    driver.find_element(by=By.LINK_TEXT, value="我的购物车").click()
    # 切换页面之后执行时需要切换句柄的
    to_new_handle(driver, index_page_handle)
    cart_page_handle = driver.current_window_handle
    print(driver.current_url)
    # 执行页面滚动
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, 9000)")
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value="售后").click()


