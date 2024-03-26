# 测试用例的组织管理

import pytest

def test_01():
    print(1)

def test_02():
    print(2)

def test_03():
    print(3)

@pytest.mark.run(order=1)
def test_04():
    print(4)

class TestLogin():
    @pytest.mark.run(order=-2)
    def test_10(self):
        print(10)
    @pytest.mark.run(order=-1)
    def test_05(self):
        print(5)
    def test_06(self):
        print(6)
    def test_07(self):
        print(7)
    def test_08(self):
        print(8)
    def test_09(self):
        print(9)



if __name__ == '__main__':
    pytest.main(["-v", "test_pytest4.py"])
    # 在pytest当中 测试方法执行顺序默认是从上到下
    # 使用pytest.mark.run进行测试函数执行顺序的标记时
    # 需要先安装pytest_ordering
    # 优先级方面pytest.mark.first是最高优先级
    # 标记顺序时，order和first last这种形式会相互冲突
