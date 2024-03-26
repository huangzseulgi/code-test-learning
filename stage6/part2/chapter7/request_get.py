import requests

# response = requests.get("https://www.baidu.com")
# print(response)
# print(response.status_code)
# print(response.text)

url = "http://localhost:5000/"
# 无参数的get请求
r1 = requests.get(url)
print(r1.text)

# 带路径的get请求
r2 = requests.get(url + "hello")
print(r2.text)

# 路径上带参数的get请求
r3 = requests.get(url + "hello/我是参数")
print(r3.text)

# 路径上带参数且带有参数值的get请求
r4 = requests.get(url + "hello/args/我是参数11?key=我是key&value=我是value")
print(r4.text)

# 第二种带参数的方式
r5 = requests.get(url + "hello/args/我是参数22", {
    "key": "我是key2",
    "value": "我是value2"})
print(r5.text)
# r5 = requests.get(url + "hello/args/参数输入查询", data={
#     "key": "我是key2",
#     "value": "我是value2"
# })
# print(r5.text)

