"""
routes/io.py — 导入导出路由（11号）
GET /api/export?format=json|csv — 导出数据
POST /api/import — 导入数据
"""

from flask import Blueprint, request, jsonify

bp = Blueprint("io", __name__, url_prefix="/api")


@bp.route("/export", methods=["GET"])
def export_data():
    """
    导出数据
    Query: format=json|csv
    JSON: 返回 JSON 附件
    CSV: 返回 CSV 附件
    """
    # TODO: 11号实现
    pass


@bp.route("/import", methods=["POST"])
def import_data():
    """
    导入数据
    请求: multipart/form-data (file 字段)
    逐行校验、去重（同金额+同日期+同类别视为重复）
    返回: {"ok": true, "imported": int, "skipped": int, "errors": [...]}
    """
    # TODO: 11号实现
    pass