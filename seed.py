"""
seed.py — 演示数据生成（11号）
15:00 前提交。生成 40 条近 3 个月记录，覆盖所有类别。
"""

# TODO: 11号实现 — 调用 storage 或直接写入 data/records.json
# 要求：40 条记录，覆盖所有支出和收入类别，日期分布在近 3 个月


def generate_seed_data() -> list[dict]:
    """生成 40 条演示记录"""
    # TODO: 11号实现
    return []


if __name__ == "__main__":
    records = generate_seed_data()
    print(f"生成了 {len(records)} 条演示记录，需写入 data/records.json")
    # TODO: 11号 — 写入数据文件