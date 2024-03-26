# filter

letter = ['a', 'B', 'c', 'D', 'e', 'F', 'g']
# 采用filter函数过滤大写字母
# 结果为True的留下，不为True的删除
upper_letter = filter(lambda x: x == x.upper(), letter)
print(upper_letter)
print(list(upper_letter))

student_name = ['李元芳', '李建国', '张三']
print(list(
    filter(lambda x: x.startswith('李'), student_name)
))
