"""test_models.py — 模型校验测试（3号）

至少 3 个测试：
1. new_record 正确生成字段
2. validate 合法数据返回 []
3. validate 非法数据返回对应中文错误
"""

import pytest


class TestModels:
    """模型模块测试"""

    def test_new_record_fields(self):
        """测试：new_record 自动生成 id、created_at，金额保留两位小数"""
        # TODO: 3号实现
        pass

    def test_validate_valid(self):
        """测试：合法数据 validate 返回 []"""
        # TODO: 3号实现
        pass

    def test_validate_invalid(self):
        """测试：非法数据 validate 返回中文错误列表"""
        # TODO: 3号实现
        pass