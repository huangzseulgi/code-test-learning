import pytest

if __name__ == '__main__':
    # 。/表示执行当前文件夹下的
    pytest.main(["-vs", "--color=yes", "-p", "no:warnings", "./"])
