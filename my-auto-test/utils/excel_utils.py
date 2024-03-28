import pandas as pd

def get_excel_case_data(interface_type):
    data = pd.read_excel("./case_data/case_data01.xlsx")   # 读取数据
    interface_type_data = data[data["请求接口类别"] == interface_type]   # 筛选数据 数据类型为DataFrame（需转换）
    return interface_type_data.to_dict(orient="records")    # 转化为列表嵌套字典类型