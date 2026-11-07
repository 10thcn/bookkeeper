"""test_storage.py — 数据存储测试（2号）

至少 3 个测试：
1. 空文件 → load_all() 返回 []
2. 正常读写流程
3. JSON 损坏 → 备份 + 返回 []
"""

import json
import sys
from pathlib import Path

import pytest

# 保证直接运行 pytest 时也能导入项目根目录下的 storage
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import storage


@pytest.fixture
def data_file(tmp_path, monkeypatch):
    """把 storage.DATA_FILE 指向临时目录，避免污染真实数据"""
    path = tmp_path / "data" / "records.json"
    monkeypatch.setattr(storage, "DATA_FILE", str(path))
    return path


class TestStorage:
    """存储模块测试"""

    def test_load_empty_file(self, data_file):
        """测试：数据文件不存在或为空时返回 []"""
        # 文件不存在 → 自动创建空数组
        assert storage.load_all() == []
        assert data_file.exists()
        assert json.loads(data_file.read_text(encoding="utf-8")) == []

        # 显式空文件 → 同样返回 []
        data_file.write_text("", encoding="utf-8")
        assert storage.load_all() == []

    def test_normal_read_write(self, data_file):
        """测试：正常追加→保存→读取流程"""
        records = [
            {
                "id": "id-1",
                "type": "expense",
                "category": "饮食",
                "amount": 25.5,
                "date": "2026-11-07",
                "note": "午饭",
                "created_at": "2026-11-07T12:00:00+00:00",
            },
            {
                "id": "id-2",
                "type": "income",
                "category": "工资",
                "amount": 8000.0,
                "date": "2026-11-01",
                "note": "",
                "created_at": "2026-11-01T09:00:00+00:00",
            },
        ]

        # save_all → load_all 内容一致，且中文原样写入（UTF-8 不转义）
        storage.save_all(records)
        assert storage.load_all() == records
        assert "饮食" in data_file.read_text(encoding="utf-8")

        # append 单条追加
        storage.append(
            {
                "id": "id-3",
                "type": "expense",
                "category": "交通",
                "amount": 3.0,
                "date": "2026-11-07",
                "note": "地铁",
                "created_at": "2026-11-07T18:00:00+00:00",
            }
        )
        loaded = storage.load_all()
        assert len(loaded) == 3
        assert loaded[-1]["id"] == "id-3"

        # update 合并 patch，未提供字段保持不变，id 不可被覆盖
        updated = storage.update("id-1", {"amount": 30.0, "id": "hacked"})
        assert updated is not None
        assert updated["id"] == "id-1"
        assert updated["amount"] == 30.0
        assert updated["note"] == "午饭"
        assert storage.update("not-exist", {"amount": 1.0}) is None

        # delete 返回 True/False，并持久化
        assert storage.delete("id-2") is True
        assert storage.delete("id-2") is False
        assert [r["id"] for r in storage.load_all()] == ["id-1", "id-3"]

    def test_corrupted_recovery(self, data_file):
        """测试：JSON 损坏时创建 .bak 备份并返回 []"""
        data_file.parent.mkdir(parents=True, exist_ok=True)
        broken = "{ 这不是合法的 JSON"
        data_file.write_text(broken, encoding="utf-8")

        assert storage.load_all() == []

        # 原始内容被备份到 .bak
        backup = Path(str(data_file) + ".bak")
        assert backup.exists()
        assert backup.read_text(encoding="utf-8") == broken

        # 数据文件已重置为合法空数组，后续读写正常
        assert json.loads(data_file.read_text(encoding="utf-8")) == []
        storage.append({"id": "id-9", "type": "expense", "category": "其他",
                        "amount": 1.0, "date": "2026-11-07", "note": "",
                        "created_at": "2026-11-07T20:00:00+00:00"})
        assert len(storage.load_all()) == 1
