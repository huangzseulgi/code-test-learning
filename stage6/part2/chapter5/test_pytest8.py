# 多fixture的应用
import pytest


@pytest.fixture()
def first_fixture():
    print("\n我是第1个fixture")
    # 多返回值
    return 1, 2, 3


@pytest.fixture()
def second_fixture(first_fixture):
    print("\n我是第2个fixture")
    return 2


# 多个参数的传入
def test_case1(first_fixture, second_fixture):
    print("这是我的第1个测试用例")
    a, b, c = first_fixture
    r = second_fixture
    print(a, b, c)
    print(r)
    assert (1, 2, 3) == (a, b, c)


if __name__ == '__main__':
    pytest.main(["-vs", "test_pytest8.py"])