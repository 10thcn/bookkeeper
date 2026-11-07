"""
storage.py — 数据存储（2号）
负责 records.json 的读写、原子替换、损坏恢复
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "records.json")


def load_all() -> list[dict]:
    """
    读取全部记录
    - 文件不存在 → 创建空数组并返回 []
    - JSON 损坏 → 备份为 .bak，返回 []
    - 返回 list[dict]
    """
    # TODO: 2号实现
    pass


def save_all(records: list[dict]) -> None:
    """
    全量保存记录（先写临时文件再 os.replace，原子替换）
    """
    # TODO: 2号实现
    pass


def append(record: dict) -> None:
    """单条追加记录"""
    # TODO: 2号实现
    pass


def update(record_id: str, patch: dict) -> dict | None:
    """
    更新记录
    - 返回更新后的记录，不存在返回 None
    """
    # TODO: 2号实现
    pass


def delete(record_id: str) -> bool:
    """
    删除记录
    - 返回 True（成功）或 False（不存在）
    """
    # TODO: 2号实现
    pass