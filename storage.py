"""
storage.py — 数据存储（2号）
负责 records.json 的读写、原子替换、损坏恢复
"""

import json
import os
import tempfile
import threading

# 数据文件路径（测试中可通过 monkeypatch 替换）
DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "records.json")

# 损坏文件的备份后缀
BACKUP_SUFFIX = ".bak"

# 读-改-写串行化，避免并发请求互相覆盖
_LOCK = threading.RLock()


def load_all() -> list[dict]:
    """
    读取全部记录
    - 文件不存在 → 创建空数组并返回 []
    - JSON 损坏 → 备份为 .bak，返回 []
    - 返回 list[dict]
    """
    path = DATA_FILE

    if not os.path.exists(path):
        _write_atomic([])
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except UnicodeDecodeError:
        # 非 UTF-8 内容同样视为损坏
        return _recover_from_corruption()

    if not text.strip():
        # 空文件按空数组处理
        return []

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return _recover_from_corruption()

    if not isinstance(data, list):
        return _recover_from_corruption()

    return data


def save_all(records: list[dict]) -> None:
    """
    全量保存记录（先写临时文件再 os.replace，原子替换）
    """
    if not isinstance(records, list):
        raise TypeError("records 必须是 list[dict]")

    with _LOCK:
        _write_atomic(records)


def append(record: dict) -> None:
    """单条追加记录"""
    with _LOCK:
        records = load_all()
        records.append(record)
        _write_atomic(records)


def update(record_id: str, patch: dict) -> dict | None:
    """
    更新记录
    - 返回更新后的记录，不存在返回 None
    """
    with _LOCK:
        records = load_all()
        for index, record in enumerate(records):
            if record.get("id") == record_id:
                merged = {**record, **(patch or {})}
                merged["id"] = record_id  # id 不允许被 patch 改写
                records[index] = merged
                _write_atomic(records)
                return merged
        return None


def delete(record_id: str) -> bool:
    """
    删除记录
    - 返回 True（成功）或 False（不存在）
    """
    with _LOCK:
        records = load_all()
        remaining = [r for r in records if r.get("id") != record_id]
        if len(remaining) == len(records):
            return False
        _write_atomic(remaining)
        return True


# ── 内部工具 ──

def _write_atomic(records: list[dict]) -> None:
    """把 records 写入临时文件，再原子替换到 DATA_FILE"""
    path = DATA_FILE
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)

    fd, tmp_path = tempfile.mkstemp(prefix=".records-", suffix=".tmp", dir=directory)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, path)
    except BaseException:
        # 写入失败时清掉临时文件，保留原数据文件
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise


def _recover_from_corruption() -> list[dict]:
    """把损坏的数据文件备份为 .bak，重置为空数组并返回 []"""
    path = DATA_FILE
    backup = path + BACKUP_SUFFIX

    try:
        os.replace(path, backup)  # 已有旧备份时会被覆盖
    except OSError:
        try:
            os.remove(path)
        except OSError:
            pass

    _write_atomic([])
    return []
