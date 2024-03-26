# 跳过测试
# @pytest.mark.skip
# @pytest.mark.skipif
import pytest
# 无条件跳过
@pytest.mark.skip
def test_01():
    assert 1==1
# 条件跳过
a = 1
@pytest.mark.skipif(a > 0, reason='a大于0跳过')
def test_02():
    assert 1==1
