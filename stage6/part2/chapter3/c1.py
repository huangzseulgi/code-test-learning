import pandas as pd

# 显示所有的列
pd.set_option('display.max_columns', None)

# 显示所有行
# pd.set_option('display.max_rows', None)

# 获取Excel数据
sheet1_data = pd.read_excel("../第三章接口测试用例.xlsx")
print(sheet1_data)