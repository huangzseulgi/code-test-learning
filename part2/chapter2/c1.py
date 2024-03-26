# def func1():
#     print("func1")
#     return func2
#
# # 函数1的返回值是函数2的引用
# def func2():
#     print("func2")
#     return 2
#
# r = func1()    # r = func2
# r2 = r()
# print(r)
# print(r2)

def func1():
    print("func1")
    def func2():
        print("func2")
    func2()
    return func2   # 这个返回值是func2的引用


r = func1()
print(r)
r()
