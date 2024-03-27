import pandas as pd

def get_excel_case_data(interface_type):
    # 读取数据
    data = pd.read_excel('./case_data/第三章接口测试用例.xlsx')
    # 数据筛选：筛选满足interface_type的数据
    interface_type_data = data[data["请求接口类别"] == interface_type]
    # 将其变化为方便取用的列表嵌套字典
    interface_type_data = interface_type_data.to_dict(orient="records")
    return interface_type_data