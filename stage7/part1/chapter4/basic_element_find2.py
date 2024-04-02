# 使用ID进行定位
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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

# 驱动
driver = webdriver.Chrome(service=service, options=option)
driver.get("https://www.jd.com")
"""
    class定位
"""
# 把浏览器最大化
driver.maximize_window()
# jd_search_input = driver.find_element(by=By.CLASS_NAME, value="text")
# jd_search_input.send_keys("电脑")
# jd_search_button = driver.find_element(by=By.CLASS_NAME, value="button")
# jd_search_button.click()


driver.find_element(by=By.LINK_TEXT, value="家用电器").click()
# 新跳出来了一个窗口 将会出现多个句柄(多个页面）
# 这个时候我们需要切换操作句柄

# 句柄切换
# 拿到所有句柄
handlers = driver.window_handles
# 遍历
for h in handlers:
    if h != driver.current_window_handle:
        driver.switch_to.window(h)
    print("当前句柄是：" + driver.title)

# 链接的模糊查找
driver.find_element(by=By.PARTIAL_LINK_TEXT, value="大").click()




