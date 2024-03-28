import requests
from config.const import URL
from conftest import get_login_data
import json
import pytest

def choose_method_and_request(if_login, uri, method, data_type, input_data, expect):
    # 获取jwt_token
    if if_login == 1:
        jwt_token = get_login_data()
        headers = {
            "jwt_token": jwt_token
        }
        if method == "get":
            response = requests.get(URL + uri, json.loads(input_data),
                                    headers=headers)
            assert 200 == response.status_code
            assert int(expect) == json.loads(response.text)["status"]

        elif method == "post":
            if data_type == "form":
                response = requests.post(URL + uri, data=json.loads(input_data),
                                         headers=headers)
            elif data_type == "json":
                response = requests.post(URL + uri, json=json.loads(input_data),
                                         headers=headers)
            assert 200 == response.status_code
            print("我得到的结果是：", response.text)
            assert int(expect) == json.loads(response.text)["status"]

    # 不需要登录的情况
    elif if_login == 0:
        if method == "get":
            response = requests.get(URL + uri, json.loads(input_data))
            assert 200 == response.status_code
            assert int(expect) == json.loads(response.text)["status"]


        elif method == "post":
            if data_type == "form":
                response = requests.post(URL + uri, data=json.loads(input_data))
            elif data_type == "json":
                response = requests.post(URL + uri, json=json.loads(input_data))
            assert 200 == response.status_code
            assert int(expect) == json.loads(response.text)["status"]