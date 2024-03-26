# 作用域与自动执行
import pytest


# 会话级别的fixture
"""
    setup和teardown中并没有session
"""
@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    print("我是会话级别的作用域")


# 模块级别的fixture
@pytest.fixture(scope="module", autouse=True)
def module_fixture():
    print("我是模块级别的作用域")


# 函数级别的fixture
"""
    无论在function或者method中都生效
"""
@pytest.fixture(scope="function", autouse=True)
def function_fixture():
    print("我是函数级别的作用域")


# 类级别的fixture
"""
    每个测试类之前都会被运行
    pytest在测试函数上会自动地把函数封装成测试类
    因此在测试函数上也会运行这个类级的fixture
"""
@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    print("我是类级别的作用域")


# 方法级别的fixture
# @pytest.fixture(scope="method", autouse=True)
# """
#     使用的最新的Python版本中，去掉了scope="method"这个作用域
#     在Python3.6上会生效
# """
# def method_fixture():
#     print("我是方法级别的作用域")


def test_case1():
    print("--------我是函的测试用例no.1--------")


def test_case2():
    print("--------我是函的测试用例no.2--------")


class TestMyClass():
    def test_of_method1(self):
        print("<<<<<<<<<<<<<我是类中的测试方法no.1>>>>>>>>>>>")

    def test_of_method2(self):
        print("<<<<<<<<<<<<<我是类中的测试方法no.2>>>>>>>>>>>")