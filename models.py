"""
models.py — 数据模型与校验（3号）
负责 Record 的创建、校验、枚举定义
"""

import uuid
from datetime import datetime, timezone

# ── 类别枚举 ──
EXPENSE_CATEGORIES = ["饮食", "交通", "购物", "娱乐", "学习", "居住", "医疗", "其他"]
INCOME_CATEGORIES = ["工资", "兼职", "理财", "其他"]

ALL_CATEGORIES = {
    "expense": EXPENSE_CATEGORIES,
    "income": INCOME_CATEGORIES,
}


def new_record(payload: dict) -> dict:
    """
    从用户数据创建完整记录对象
    - 自动生成 id (UUID4)
    - 自动生成 created_at (ISO 8601)
    - 金额保留两位小数
    - 返回 dict
    """
    # TODO: 3号实现
    pass


def validate(payload: dict) -> list[str]:
    """
    校验记录数据
    - type 必须为 expense 或 income
    - amount 必须 >0
    - date 必须为 YYYY-MM-DD 格式
    - category 必须在对应枚举中
    - note 不超过 100 字
    - 返回中文错误列表，无错误时返回 []
    """
    # TODO: 3号实现
    pass