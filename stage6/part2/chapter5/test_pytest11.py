# fixture的参数化
import pytest

test_data = [
    {
        "case_name": "登录成功的测试",
        "username": "admin",
        "password": "123"
    },
    {
        "case_name": "登录失败的测试",
        "username": "user1",
        "password": "123"
    },
{
        "case_name": "用户名为空的测试",
        "username": "",
        "password": "123"
    }
]

@pytest.fixture(params=test_data)
def param_data(request):
    return request.param

def test_login(param_data):
    # 根据打印结果可知 param_data是一个字典
    # print(param_data, type(param_data))
    case_name = param_data.get('case_name')
    print(case_name)
    username = param_data.get('username')
    print(username)
    password = param_data.get('password')
    print(password)


