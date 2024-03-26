from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world qqqqqqq"

@app.route("/hello")
def hello_world2():
    return "hello22222"

@app.route("/hello/<username>")
def hello_world3(username):
    print(username)
    return "hello22222" + username

@app.route("/hello/args/<username>")
def hello_world4(username):
    print(username)
    key = request.args.get("key")
    value = request.args.get("value")
    print(key)
    print(value)
    return "hello22222" + username + "::::" + key + "::::" + value


@app.route("/mypost", methods=["post"])
def my_post():
    return "post request"

@app.route("/mypost1", methods=["post"])
def my_post1():
    # 表单数据类型
    username = request.form["username"]
    sex = request.form["sex"]
    print(username)
    print(sex)
    return "post request" + username + "::" +sex


@app.route("/mypost2", methods=["post"])
def my_post2():
    # json数据格式
    request_data = request.get_json()
    print(request_data)
    print(request_data["user"])
    return "post request" + str(request_data)


if __name__ == "__main__":
    app.run()

