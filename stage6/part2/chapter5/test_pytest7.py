import pytest


@pytest.fixture()
def first_fixture():
    print("这是我人生中第1个fixture")
    return 1


@pytest.fixture()
def second_fixture(first_fixture):
    print("这是我人生中第2个fixture")
    return first_fixture + 2


def test_case1(first_fixture):
    print("这是我的第1个测试用例")
    r = first_fixture
    print(r)


def test_case2(second_fixture):
    print("这是我的第2个测试用例")
    r = second_fixture
    print(r)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_pytest7.py'])
