# 使用ID进行定位
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_testing_path = r"E:\chrome-win64\chrome.exe"
chromedriver = r"E:\chromedriver-win64\chromedriver.exe"

# option
option = webdriver.ChromeOptions()
option.binary_location = chrome_testing_path
# 设定只打开一次：首先在命令行终端先打开这个浏览器
# E:\chrome-win64\chrome.exe --remote-debugging-port=9222
# --user-data-dir="E:\chromedriver-win64\selenium_automationProfile"
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# 设定打开浏览器之后不会自己关闭
option.add_experimental_option("detach", True)
# 隐藏正在收到自动测试软件的控制这句话
option.add_experimental_option('excludeSwitches',
                               ['enable-automation'])

# service
service = Service(chromedriver)


# 切换句柄的函数
def to_new_handler(driver, *have_handles):
    # 注意：拿到所有handlers是window_handlers
    handles = driver.window_handles
    for h in handles:
        if h not in have_handles:
            driver.switch_to.window(h)
    return driver
# 驱动
driver = webdriver.Chrome(service=service, options=option)
driver.get("https://www.jd.com")

# 把浏览器最大化
# driver.maximize_window()
# jd_search_input = driver.find_element(by=By.CLASS_NAME, value="text")
# jd_search_input.send_keys("电脑")
# jd_search_button = driver.find_element(by=By.CLASS_NAME, value="button")
# jd_search_button.click()

index_page_handle = driver.current_window_handle

driver.find_element(by=By.LINK_TEXT, value="家用电器").click()
to_new_handler(driver, index_page_handle)
print("现在的页面是：", driver.title)


jiadian_handle = driver.current_window_handle
# 链接的模糊查找
driver.find_element(by=By.PARTIAL_LINK_TEXT, value="大").click()
to_new_handler(driver, index_page_handle, jiadian_handle)
print("现在的页面是：", driver.title)

# 通过句柄来关闭页面
driver.close()

driver.switch_to.window(jiadian_handle)
driver.close()

time.sleep(3)
driver.quit()
