"""
    用于放置可能会使用的全局函数
"""


def to_new_handle(driver, *handles):
    for h in driver.window_handles:
        if h not in handles:
            driver.switch_to.window(h)
    return driver
