import time
import random

# runtime函数的引用场景为诶计算每个函数的运行时间
# 定义跑道长度
track_length = 10

# 闭包就是装饰器
def runtime(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(func.__name__,'运行时间是', end_time - start_time, '秒')
    return wrapper

@ runtime
# 使用装饰器将下面的函数传入runtime
def tortoise():
    for i in range(1, track_length+1):
        print('乌龟跑的{}米'.format(i))
        time.sleep(1)   # 每1秒跑一步

@ runtime
def rabbit():
    for i in range(1, track_length+1):
        if i % 5 == 0:   # 每1秒跑5步 然后随机休息1-10秒
            time.sleep(random.randint(1,10))
        print('兔子跑的{}米'.format(i))

tortoise()
rabbit()