import pytest


# 开头不是test的函数 在使用pytest的时候不会被测试
def add(a, b):
    return a + b


def test_dengyu():
    assert 3 == add(1, 2)


def test_budengyu():
    assert 5 == add(1, 3)


def test_dayu():
    assert 5 > add(1, 3)


def test_dayudengyu():
    assert 5 >= add(1, 3)


def test_xiaoyu():
    assert 1 < add(1, 2)


def test_xiaoyudengyu():
    assert 1 <= add(1, 3)


def test_baohan():
    assert 1 in [1, 2, 3]


def test_bubaohan():
    assert 1 not in [1, 2, 3]


def test_ifture():
    assert bool(1) is True


def test_iffalse():
    assert bool(0) is False


if __name__ == '__main__':
    pytest.main(['test_pytest13.py', "--alluredir", "./result"])

