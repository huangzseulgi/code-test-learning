# https://www.w3school.com.cn/xpath/index.asp
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 跳转到最新的页面上
def to_new_handler(driver, *have_handlers):
    handlers = driver.window_handles
    for h in handlers:
        if h not in have_handlers:
            driver.switch_to.window(h)
    return driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches',
                                       ['enable-automation'])
service = Service("../../chromedriver.exe")

driver = webdriver.Chrome(service=service,options=chrome_options)
driver.get("https://www.jd.com")
driver.find_element(by=By.XPATH,value="//*[@id='J_cate']/ul/li[1]/a").click()

index_page_handler = driver.current_window_handle
to_new_handler(driver,index_page_handler)
print("当前页面是：" + driver.title)

jiadian_element = driver.find_element(by=By.XPATH,
                         value="//*[@id=\"app\"]/div/div[2]/div/div[1]/div[1]/div/div/div/div/div/ul/li[1]/a")
jiadian_handler = driver.current_window_handle
jiadian_element.click()

to_new_handler(driver,index_page_handler,jiadian_handler)
print("当前页面是：" + driver.title)

driver.execute_script("window.scrollBy(0,800)")
time.sleep(3)

tv_handler = driver.current_window_handle
driver.find_element(by=By.XPATH,
                    value="//div[@uuid='1585301121700']/div[2]/div/div/div[1]/div").click()

to_new_handler(driver,index_page_handler,jiadian_handler,tv_handler)

print("当前页面是：" + driver.title)
driver.close()
driver.switch_to.window(tv_handler)
driver.close()
driver.switch_to.window(jiadian_handler)
driver.close()
time.sleep(2)
driver.quit()
