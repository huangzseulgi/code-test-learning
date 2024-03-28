import requests
import pytest
import json
from config.const import URL

uri = "/loginWithJwt"
login_data = {
    "userName": "imooc",
    "password": "12345678"
}

# @pytest.fixture(scope="session", autouse=True)
def get_login_data():
    response = requests.get(URL + uri, login_data)
    # 查询response之后发现是str 所以要用json来loads
    data = json.loads(response.text)
    jwt_token = data['data']
    # print(response.text)
    return jwt_token
