"""
routes/records.py — 记账模块路由（4号）
POST /api/records — 新增记录
PUT /api/records/<id> — 更新记录
DELETE /api/records/<id> — 删除记录
"""

from flask import Blueprint, request, jsonify

bp = Blueprint("records", __name__, url_prefix="/api/records")


@bp.route("", methods=["POST"])
def create_record():
    """
    新增一条记录
    请求体: {type, category, amount, date, note?}
    返回: 201 {"ok": true, "record": {...}}
    错误: {"ok": false, "errors": [...]}
    """
    # TODO: 4号实现 — 1) validate(payload) 2) new_record(payload) 3) storage.append(record) 4) 返回 201
    pass


@bp.route("/<record_id>", methods=["PUT"])
def update_record(record_id):
    """
    更新记录（部分或全部字段）
    请求体: 部分或全部字段
    返回: {"ok": true, "record": {...}}
    """
    # TODO: 4号实现
    pass


@bp.route("/<record_id>", methods=["DELETE"])
def delete_record(record_id):
    """
    删除记录
    返回: {"ok": true}
    """
    # TODO: 4号实现
    pass