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

@ app.route('/start')
def hello_world2():
    return 'Hello, world2'

@ app.route('/hello/args/<username>')
def hello_world5(username):
    print(username)
    key = request.args.get('key')
    print(key)
    value = request.args.get('value')
    print(value)
    return 'Hello, world2' + username + '::::' + key + '::::' + value

# route中method默认为get,因此除了get无需声明外其他均需要声明
@app.route('/mypost', methods=['post'])
def my_post():
    return 'post request'

@app.route('/mypost1', methods=['post'])
def my_post_form():
    # 表单数据类型
    username = request.form['username']
    sex = request.form['sex']
    print(username)
    print(sex)
    return 'post request' + ':::' + username + ':::' + sex

@app.route('/mypost2', methods=['post'])
def my_post_json():
    # json数据
    request_data = request.get_json()
    print(request_data)
    print(request_data["user"])
    return 'post request' + str(request_data)

if __name__ == '__main__':
    # 启动flask
    app.run()