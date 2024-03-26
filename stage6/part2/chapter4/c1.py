import pymysql
import pandas as pd

# 数据库的连接诶信息
db_info = {
    "host": "10.4.179.121",
    "user": "root",
    "password": "123",
    "database": "mydb2",
    "charset": "utf8"
}

#  **db_info ：将字典键值对逐个解析
conn = pymysql.connect(**db_info)
cursor = conn.cursor()
sql = "select * from mumu"
cursor.execute(sql)
#  此处打印将得到结果的数目信息
# res = cursor.fetchall()
# # 数据类型为元组
# print(res)
res = pd.read_sql(sql, conn)
print(res)
# 类型为：<class 'pandas.core.frame.DataFrame'>
# 因此可以用pandas进行数据的访问 过滤 筛选
print(type(res))