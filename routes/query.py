"""
routes/query.py — 查看模块路由（5号）
GET /api/records — 分页查询（支持筛选、排序、关键字搜索）
GET /api/records/<id> — 单条详情
"""

from flask import Blueprint, request, jsonify

bp = Blueprint("query", __name__, url_prefix="/api/records")


@bp.route("", methods=["GET"])
def list_records():
    """
    分页查询记录
    Query 参数:
      type        — expense / income（筛选类型）
      category    — 类别筛选
      date_from   — 起始日期 YYYY-MM-DD
      date_to     — 结束日期 YYYY-MM-DD
      q           — 关键字搜索（匹配 note）
      sort        — date_asc / date_desc / amount_asc / amount_desc
      page        — 页码（默认 1）
      page_size   — 每页条数（默认 10）
    返回: {"ok": true, "items": [...], "total": int, "page": int, "pages": int}
    """
    # TODO: 5号实现
    pass


@bp.route("/<record_id>", methods=["GET"])
def get_record(record_id):
    """
    获取单条记录详情
    返回: 记录对象 或 404
    """
    # TODO: 5号实现
    pass