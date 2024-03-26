import pandas as pd

# 显示所有的列
pd.set_option('display.max_columns', None)

# 显示所有行
# pd.set_option('display.max_rows', None)

# 获取Excel数据
sheet1_data = pd.read_excel("../第三章接口测试用例.xlsx")

# 获取某个sheet的数据 sheet_name字段
# sheet2_data = pd.read_excel("../第三章接口测试用例.xlsx", sheet_name='Sheet2')

print(sheet1_data)
print(type(sheet1_data))

# 单独访问一列数据
nums = sheet1_data['编号']
print(nums)
print(type(nums))

# 访问多列
nums2 = sheet1_data[['编号', '标题']]
print(nums2)

# 访问行的数据
nums3 = sheet1_data['编号'][0]
print(nums3)

# 访问多行多列
nums4 = sheet1_data[['编号', '标题']][1:4]
print(nums4)

# 单独访问行数据 通过索引来访问 先行后列
nums5 = sheet1_data.iloc[[1]]
print(nums5)

# 访问某几行和某几列
nums6 = sheet1_data.iloc[[1, 3], [2, 3]]
print(nums6)

# 访问某几行到某几列
nums7 = sheet1_data.iloc[1:3, 2:3]
print(nums7)
