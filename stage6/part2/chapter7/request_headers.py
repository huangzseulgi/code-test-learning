import requests
import json
url = "http://111.231.103.117:8083"
login_url = "/loginWithJwt"
login_data ={
    "userName": "imooc",
    "password": "12345678"
}
login_response = requests.get(url + login_url, login_data)
# print(login_response.status_code)
# 直接得到的是一个str 如果要从里面取值的话要用JSON转换
# print(login_response.text, type(login_response.text))
data = json.loads(login_response.text)
print(data, type(data))
jwt_token = data['data']
print(jwt_token, type(jwt_token))

# 请求头信息(自定义）
headers = {
    "jwt_token": jwt_token
}

cart_add_url = "/cart/add"
cart_add_data = {
    "count": 5,
    "productId": 41
}

cart_add_response = requests.post(url + cart_add_url, data=cart_add_data, headers=headers)
print(cart_add_response.text)


