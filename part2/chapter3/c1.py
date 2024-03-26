# 匿名函数lambda
# 计算圆形面积
# pi * r * r
import math
def circle_area(r):
    res = math.pi * r * r
    return res
res =  circle_area(2)
print(res)

# 匿名函数:可以看做是一行公式
res = lambda r: math.pi * r * r
print(res(2))

# 用一行代码实现了比较复杂的一个运算
def calculate(o):
    if o == "+":
        return lambda a,b : a + b
    elif o == "-":
        return lambda a, b: a - b
    elif o == "*":
        return lambda a, b: a * b
    elif o == "/":
        return lambda a, b: a / b
f = calculate("/")
print(f)
print(f(3, 4))