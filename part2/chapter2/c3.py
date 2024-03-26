"""
    yield关键字的使用：
    采用for循环调用
"""
def func1():
    return "haha"
    print("不会被打印")

def func2():
    print("1")
    yield "y1"
    print("2")
    print("3")
    yield "y2"
    print("4")
    yield None
    print("5")
    yield "y2"


r2 = func2()
for i in r2:
    print('————————————————')


