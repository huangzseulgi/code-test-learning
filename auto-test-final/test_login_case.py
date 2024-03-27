# 使用数据库原生结合fixture实现自动化测试

import pytest
import utils.mysql_utils as um
import utils.excel_utils as ue
import requests
import json

url = "http://111.231.103.117:8083"

# """
#     1、使用数据库原生结合fixture实现自动化测试(即不使用pandas)
# """
# @pytest.fixture(params=um.get_mysql_case_data("登录"))
# def get_mysql_login_data(request):
#     return request.param
#
#
# def test_mysql_login1(get_mysql_login_data):
#     # get_mysql_login_data函数的最终结果是一个元组
#     # 但每次测试用例调用的时候只会传过来一条测试用例
#     # 因此可以按字段取值
#     id = get_mysql_login_data[0]
#     case = get_mysql_login_data[1]
#     title = get_mysql_login_data[2]
#     interface_type = get_mysql_login_data[3]
#     uri = get_mysql_login_data[4]
#     method = get_mysql_login_data[5]
#     if_login = get_mysql_login_data[6]
#     input_data = get_mysql_login_data[7]
#     data_type = get_mysql_login_data[8]
#     expect = get_mysql_login_data[9]
#
#     if method == "get":
#         response = requests.get(url + uri, json.loads(input_data))
#         print(response.text)
#         assert 200 == response.status_code
#         # 返回的值是一个json(str) 因此要load为字典
#         assert int(expect) == json.loads(response.text)["status"]
#
#     elif method == "post":
#         if data_type == 'form':
#             response = requests.post(url + uri, data=json.loads(input_data))
#         elif data_type == 'json':
#             response = requests.post(url + uri, json=json.loads(input_data))
#         assert 200 == response.status_code
#         assert int(expect) == json.loads(response.text)["status"]
#
#
# """
#     2、使用数据库pandas结合fixture实现自动化测试
# """
# @pytest.fixture(params=um.get_mysql_case_data_for_pandas("登录"))
# def get_mysql_login_data_for_pandas(request):
#     return request.param
#
#
# def test_mysql_login2(get_mysql_login_data_for_pandas):
#     # 同样的 每次测试用例调用的时候只会传一条数据过来
#     # print(get_mysql_login_data_for_pandas)
#     if get_mysql_login_data_for_pandas["method"] == "get":
#         response = requests.get(url + get_mysql_login_data_for_pandas["uri"],
#                                 json.loads(get_mysql_login_data_for_pandas["input_data"]))
#         # print(type(response.text))
#         assert 200 == response.status_code
#         # response的值是一个str 因此需要先json.load转化为dict
#         assert int(get_mysql_login_data_for_pandas["expect"]) == json.loads(response.text)["status"]
#
#     elif get_mysql_login_data_for_pandas["method"] == "post":
#         # 不管输入数据是什么都是需要json.loads的, 因为input_data本身就是一个json数据
#         # 区别在于使用get的时候不区分数据类型直接json.loads
#         # 而使用post时需要区分form和json, 分别用data=和json=传参
#         if get_mysql_login_data_for_pandas["data_type"] == "form":
#             response = requests.post(url + get_mysql_login_data_for_pandas["uri"],
#                                      data=json.loads(get_mysql_login_data_for_pandas["input_data"]))
#         elif get_mysql_login_data_for_pandas["data_type"] == "json":
#             response = requests.post(url + get_mysql_login_data_for_pandas["uri"],
#                                      json=json.loads(get_mysql_login_data_for_pandas["input_data"]))
#
#         assert 200 == response.status_code
#         assert int(get_mysql_login_data_for_pandas["expect"]) == json.loads(response.text)["status"]

# """
#     3、使用参数化的方式获取excel表中的测试用例数据
# """
# @pytest.mark.parametrize(['case_id',
#                           'title',
#                           'interface_type',
#                           'uri',
#                           'method',
#                           'if_login',
#                           'input_data',
#                           'data_type',
#                           'expect'], ue.get_excel_case_data("登录"))
# def test_excel_data_login(case_id, title, interface_type, uri, method,
#                          if_login, input_data, data_type, expect):
#     if method == "get":
#         response = requests.get(url + uri, json.loads(input_data))
#         print(response.text)
#         assert 200 == response.status_code
#         # 返回的值是一个json(str) 因此要load为字典
#         assert int(expect) == json.loads(response.text)["status"]
#
#     elif method == "post":
#         if data_type == 'form':
#             response = requests.post(url + uri, data=json.loads(input_data))
#         elif data_type == 'json':
#             response = requests.post(url + uri, json=json.loads(input_data))
#         assert 200 == response.status_code
#         assert int(expect) == json.loads(response.text)["status"]


