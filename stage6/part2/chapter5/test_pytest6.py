# pytest的前置和后置操作
import pytest
"""
1. 在Python3.6的版本中可以运行setup和teardown函数，但是优先级没有下面这几个函数的优先级高；
2. 模块级别的函数，前置在测试前运行，后置在测试后运行；
3. 函数级别的函数，前置和后置分别在每次测试函数的运行前后运行。
"""

def setup_module():
    print("这是前置的模块级别的函数")

def teardown_module():
    print("这是后置的模块级别的函数")

def setup_function():
    print("这是前置的函数级别的函数")

def teardown_function():
    print("这是后置的函数级别的函数")

def test_01():
    print("测试1运行了")
    assert 1==1

def test_02():
    print("测试2运行了")
    assert 2==2

class TestMyClass():
    def setup_class(self):
        print("这是前置的class级别的方法")
    def teardown_class(self):
        print("这是后置的class级别的方法")
    def setup_method(self, method):
        print("这是前置的method级别的方法")
    def teardown_method(self, method):
        print("这是后置的method级别的方法")

    def test_of_method1(self):
        print("类中的方法1测试了")
    def test_of_method2(self):
        print("类中的方法2测试了")


if __name__ == '__main__':
    # pytest中不会输出print的打印结果
    pytest.main(["-s", "-v", "test_pytest6.py"])