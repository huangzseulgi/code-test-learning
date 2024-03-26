import pandas as pd

# 显示所有的列
pd.set_option('display.max_columns', None)

# 显示所有行
# pd.set_option('display.max_rows', None)

# 获取Excel数据
sheet1_data = pd.read_excel("../第三章接口测试用例.xlsx")

# 按照列依次访问
for i in sheet1_data:
    print(i)
    print(sheet1_data[i])

# 按照行依次访问
for i in sheet1_data.index:
    print(i)
    print(sheet1_data.iloc[[i]])

# 按照每个元素依次访问
for i in sheet1_data.index:          # i行
    for j in sheet1_data.iloc[[i]]:  # j列
        print(sheet1_data[j][i])     # 列，行