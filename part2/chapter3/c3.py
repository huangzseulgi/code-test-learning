# reduce
from functools import reduce
a = [2, 4, 6, 8, 10]

def add(x, y):
    print("x是{}，y是{}".format(x, y))
    return x + y

res = reduce(add, a)
print(res)

res1 = reduce(lambda x,y : x + y, a)
print(res1)