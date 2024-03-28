import pytest
import utils.mysql_utils as um
import utils.excel_utils as ue
from utils.method_choose import choose_method_and_request
import requests
from config.const import URL
import json
from conftest import get_login_data

"""
    MySQL数据参数化和测试
"""

# # 1. parameterize
# @pytest.mark.parametrize(['id',
#                           'case_id',
#                           'title',
#                           'interface_type',
#                           'uri',
#                           'method',
#                           'if_login',
#                           'input_data',
#                           'data_type',
#                           'expect'], um.get_mysql_case_data("登录"))
# def test_login_case_mysql_params(id, case_id, title, interface_type, uri, method, if_login,
#                                  input_data, data_type, expect):
#     # 注意：数据库原生方法获取的数据就是测试用例本身，不包含表头
#     # 因此不是key:value而是value
#     choose_method_and_request(int(if_login),
#                               uri,
#                               method,
#                               data_type,
#                               input_data,
#                               expect)
# #
# #
# # 2. fixture
# @pytest.fixture(params=um.get_mysql_case_data("登录"))
# def get_param(request):
#     print(request.param)
#     return request.param
#
#
# def test_login_case_mysql_fixture(get_param):
#     # 同样的 当采用数据库原生方法时 因为没有Key 所以要考索引来获取各个值
#     choose_method_and_request(if_login=int(get_param[6]),
#                               uri=get_param[4],
#                               method=get_param[5],
#                               data_type=get_param[8],
#                               input_data=get_param[7],
#                               expect=get_param[9])

# pandas+fixture
@pytest.fixture(params=um.get_mysql_case_data_for_pandas("购物车"))
def get_param_mysql_pandas(request):
    return request.param

def test_login_case_excel_params(get_param_mysql_pandas):
    # print(get_param_mysql_pandas)
    # assert 1 == 2
    id = get_param_mysql_pandas["id"]
    case_id = get_param_mysql_pandas["case_id"]
    title = get_param_mysql_pandas["title"]
    interface_type = get_param_mysql_pandas["interface_type"]
    uri = get_param_mysql_pandas["uri"]
    method = get_param_mysql_pandas["method"]
    if_login = get_param_mysql_pandas["if_login"]
    input_data = get_param_mysql_pandas["input_data"]
    data_type = get_param_mysql_pandas["data_type"]
    expect = get_param_mysql_pandas["expect"]

    choose_method_and_request(if_login=int(if_login),
                              uri=uri,
                              method=method,
                              data_type=data_type,
                              input_data=input_data,
                              expect=expect)

"""
    Excel数据参数化和测试
"""


# # 1. fixture
# @pytest.fixture(params=ue.get_excel_case_data("登录"))
# def get_param_excel(request):
#     return request.param
#
# def test_login_case_excel_params(get_param_excel):
#     case_id = get_param_excel["编号"]
#     title = get_param_excel["标题"]
#     interface_type = get_param_excel["请求接口类别"]
#     uri = get_param_excel["请求地址"]
#     method = get_param_excel["请求方式"]
#     if_login = get_param_excel["是否需要登录"]
#     input_data = get_param_excel["输入数据"]
#     data_type = get_param_excel["数据格式"]
#     expect = get_param_excel["期望结果"]
#     choose_method_and_request(if_login=if_login,
#                               uri=uri,
#                               method=method,
#                               data_type=data_type,
#                               input_data=input_data,
#                               expect=expect)

