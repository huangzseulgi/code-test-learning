from flask import Flask, request

# 固定格式：获取flask对象
app = Flask(__name__)

# @ app.route('/')
# def hello_world():
#     return 'Hello, world'

# @ app.route('/hello')
# def hello_world2():
#     return 'Hello, world2'
#
# @ app.route('/hello/<username>')
# def hello_world3(username):
#     print(username)
#     return 'Hello, world2' + username
#
# @ app.route('/hello/args/<username>')
# def hello_world4(username):
#     print(username)
#     key = request.args.get('key')
#     print(key)
#     return 'Hello, world2' + username + '::::' + key
#
@ app.route('/hello/args/<username>')
def hello_world5(username):
    print(username)
    key = request.args.get('key')
    print(key)
    value = request.args.get('value')
    print(value)
    return 'Hello, world2' + username + '::::' + key + '::::' + value

if __name__ == '__main__':
    # 启动flask
    app.run()