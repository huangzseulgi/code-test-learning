import pandas as pd
import json

# 显示所有的列
pd.set_option('display.max_columns', None)

# 显示所有行
# pd.set_option('display.max_rows', None)

# 获取Excel数据
sheet1_data = pd.read_excel("../第三章接口测试用例.xlsx")

# 数据的筛选：登录
login_case_type = sheet1_data[sheet1_data["请求接口类别"] == "登录"]
# print(login_case_type, type(login_case_type))

# 数据访问：输入数据
login_case_data = login_case_type["输入数据"][0]
print(type(login_case_data))

# JSON数据转化为字典数据 JSON.load(JSON的Str)
login_case_dict = json.loads(login_case_data)
print(login_case_dict, type(login_case_dict))
# 可以访问咯
print(login_case_dict['userName'])
print(login_case_dict['password'])
