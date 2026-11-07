"""test_storage.py — 数据存储测试（2号）

至少 3 个测试：
1. 空文件 → load_all() 返回 []
2. 正常读写流程
3. JSON 损坏 → 备份 + 返回 []
"""

import pytest


class TestStorage:
    """存储模块测试"""

    def test_load_empty_file(self):
        """测试：数据文件不存在或为空时返回 []"""
        # TODO: 2号实现
        pass

    def test_normal_read_write(self):
        """测试：正常追加→保存→读取流程"""
        # TODO: 2号实现
        pass

    def test_corrupted_recovery(self):
        """测试：JSON 损坏时创建 .bak 备份并返回 []"""
        # TODO: 2号实现
        pass