"""
    conftest中可以放置一些公共的fixture
    在其他.py文件中就可以直接去调用
    甚至不需要去import!!
"""
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