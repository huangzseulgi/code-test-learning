import pytest
import requests
import json
from config.const import URL
import utils.mysql_utils as um
import utils.excel_utils as ue

@pytest.fixture()
def get_token(get_login_token):
    return get_login_token

@pytest.fixture()
def get_params():
    return ue.get_excel_case_data("购物车")

def test_excel_cart_add(get_token, get_params):
    params = get_params
    jwt_token = get_token
    for requests_data in params:
        case_id = requests_data['编号']
        title = requests_data['标题']
        interface_type = requests_data['请求接口类别']
        uri = requests_data['请求地址']
        method = requests_data['请求方式']
        if_login = requests_data['是否需要登录']
        input_data = requests_data['输入数据']
        data_type = requests_data['数据格式']
        expect = requests_data['期望结果']
        if if_login == 1:
            headers = {
                "jwt_token":jwt_token
            }
            if method == 'get':
                response = requests.get(URL + uri,
                                        input_data,
                                        headers=headers)
                assert 200 == response.status_code
                assert int(expect) == json.loads(response.text)['status']
            elif method == 'post':
                if data_type == "form":
                    response = requests.get(URL + uri,
                                            data=input_data,
                                            headers=headers)
                elif data_type == "json":
                    response = requests.get(URL + uri,
                                            json=input_data,
                                            headers=headers)
                assert 200 == response.status_code
                assert int(expect) == json.loads(response.text)['status']

        elif if_login == 0:
            if method == 'get':
                response = requests.get(URL + uri,
                                        input_data,
                                        headers=headers)
                assert 200 == response.status_code
                assert int(expect) == json.loads(response.text)['status']
            elif method == 'post':
                if data_type == "form":
                    response = requests.get(URL + uri,
                                            data=input_data)
                elif data_type == "json":
                    response = requests.get(URL + uri,
                                            json=input_data)
                assert 200 == response.status_code
                assert int(expect) == json.loads(response.text)['status']




