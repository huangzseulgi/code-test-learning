import pymysql
from flask import Flask, request

# 这里是MySQL的基本连接信息
conn = pymysql.connect(
    host='10.4.179.121',
    user='root',
    password='123',
    database='mydb1',
    charset='utf8'
)

cursor = conn.cursor()

# 固定格式：获取flask对象
app = Flask(__name__)

@ app.route('/')
def hello_world():
    sql = 'select * from school'
    # res会显示查询到了几条数据 是一个int
    res = cursor.execute(sql)
    # 得到真正的结果
    r = cursor.fetchall()
    print(r)
    # 返回值不能是int
    return str(r)

if __name__ == '__main__':
    # 启动flask
    app.run()