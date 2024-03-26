# map函数

my_list = [1, 2, 3, 4, 5]
# 将所有元素执行加1操作
# 方法1 遍历
res = []
for i in range(len(my_list)):
    res.append(my_list[i]+1)
    print(res)

# 方法2 map函数
def add_one(e):
    return e + 1
r = map(add_one, my_list)
# map会将数据拆分成，并一个一个操作，如下：
# [2, 3]
# [2, 3, 4]
# [2, 3, 4, 5]
# [2, 3, 4, 5, 6]
print(list(r))

# 方法3 map + lambda
print(list(map(lambda e: e + 1, my_list)))