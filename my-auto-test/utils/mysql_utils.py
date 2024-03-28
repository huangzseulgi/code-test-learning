import pymysql
import pandas as pd
# 数据库连接信息
db_info = {
    "host": "10.4.179.121",
    "user": "root",
    "password": "123",
    "database": "mydb2",
    "charset": "utf8"
}

# 连接
def get_mysql_case_data(interface_type):
    conn = pymysql.connect(**db_info)   # **用于解包 将字典中的数据逐个解出并传给connect
    cursor = conn.cursor()
    sql = "select * from mumu where interface_type = '{}'".format(interface_type)
    cursor.execute(sql)       # 执行sql语句
    data = cursor.fetchall()   # 抓取数据 此时抓取到的数据是元组类型(不能转化为字典哈）
    return data

def get_mysql_case_data_for_pandas(interface_type):
    conn = pymysql.connect(**db_info)
    sql = "select * from mumu where interface_type = '{}'".format(interface_type)
    data = pd.read_sql(sql, conn)   # 获取的数据是DataFrame 需要转化为列表嵌套字典
    return data.to_dict(orient="records")

# print(get_mysql_case_data("登录"))
