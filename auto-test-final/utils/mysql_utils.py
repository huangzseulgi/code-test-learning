import pymysql
import pandas as pd

def mysql_connection():
    db_info = {
        "host": "10.4.179.121",
        "user": "root",
        "password": "123",
        "database": "mydb2",
        "charset": "utf8"
    }
    conn = pymysql.connect(**db_info)
    return conn


def get_mysql_case_data(interface_type):
    # 传一个接口类型的参数用于取数据库中的数据
    conn = mysql_connection()
    sql = "select * from mumu where interface_type = '{}'".format(interface_type)
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()

    return res


def get_mysql_case_data_for_pandas(interface_type):
    conn = mysql_connection()
    sql = "select * from mumu where interface_type = '{}'".format(interface_type)
    # 注意注意 第一个是sql 第二个是conn
    interface_type_data = pd.read_sql(sql, conn)

    # 解析数据
    final_data = interface_type_data.to_dict(orient="records")
    # final_data = []
    # # index是行索引(仅仅只是索引）
    # for i in interface_type_data.index:
    #     inner_data = {}
    #     # iloc是根据这个索引i来取出第i行的所有数据是一个Series
    #     # 因此采用d来遍历时，我们得到的是key的值
    #     # 当i不变即在i行取数据时 我们就可以根据这个key的变化得到所有值
    #     for d in interface_type_data.iloc[[i]]:
    #         inner_data[d] = interface_type_data[d][i]
    #     final_data.append(inner_data)
    return final_data
