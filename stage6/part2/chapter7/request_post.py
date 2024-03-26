import requests

url = 'http://127.0.0.1:5000/'
# 无参数post请求
r1 = requests.post(url + "mypost")
print(r1.status_code)

# 请求数据是表单类型的数据
r2 = requests.post(url + "mypost1",
                   data={
                       "username": "我是名字",
                       "sex": "我是性别"
                   })
print(r2)

# 请求数据是JSON类型的数据
r3 = requests.post(url + "mypost2",
                   json={
                       "user": "我是JSON的user的key",
                       "value": "我是value"
                   })
print(r3.text)

# requests发送请求头信息
