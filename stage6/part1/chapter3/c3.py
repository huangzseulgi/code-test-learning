from flask import Flask, request

app = Flask(__name__)


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
    return 'post request'

@app.route('/mypost2', methods=['post'])
def my_post_json():
    # json数据
    request_data = request.get_json()
    print(request_data)
    print(request_data['user'])
    return 'post request' + str(request_data)

if __name__ == '__main__':
    # 端口号是可以自定义的
    app.run(port=8080)