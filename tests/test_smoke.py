"""脚手架冒烟测试。"""

from src.main import main


def test_main_returns_zero() -> None:
    """入口函数应正常返回退出码 0。"""
    assert main() == 0
