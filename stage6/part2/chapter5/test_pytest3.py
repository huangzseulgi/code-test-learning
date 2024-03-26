import pytest
import pymysql
import pandas
db_info = {
    "host": "10.4.179.121",
    "user": "root",
    "password": "123",
    "database": "mydb2",
    "charset": "utf8"
}
conn = pymysql.connect(**db_info)
cursor = conn.cursor()
sql = "select * from mumu"
cursor.execute(sql)
res = cursor.fetchall()
# print(res)

# 把存储在mysql中的测试用例参数化
@pytest.mark.parametrize([
    'id',
    'case_id',
    'title',
    'interface_type',
    'url',
    'method',
    'if_login',
    'input_data',
    'data_type',
    'expect'
], res)
def test_py_mysql_param(id, case_id, title, interface_type, url,
                        method, if_login, input_data, data_type, expect):

    print(title)

# def add(a, b):
#     return a + b
#
#
# # 参数化实现方法1
# # (1, 2)第一组 1对应x, 2对应y
# # (0, 3)第一组 0对应x, 3对应y
# @pytest.mark.parametrize(['x', 'y'], [(1, 2), (0, 3), (0, 4)])
# def test_add1(x, y):
#     assert 3 == add(x, y)
#
#
# # 参数化实现方法2：注意 参数必须为列表,元组等可迭代对象
# xy = [(-1, 3), (-1, 4), (-1, -4)]
#
#
# @pytest.mark.parametrize(['x', 'y'], xy)
# def test_add1(x, y):
#     assert 3 == add(x, y)


if __name__ == '__main__':
    pytest.main(['--color=yes',  '-v', 'test_pytest3.py'])
