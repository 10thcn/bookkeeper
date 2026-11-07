"""
stats/category.py — 按类别维度统计（7号）
GET /api/stats/by-category?type=expense|income&from=&to=
"""

from flask import Blueprint, request, jsonify

bp = Blueprint("stats_category", __name__, url_prefix="/api/stats")


@bp.route("/by-category", methods=["GET"])
def stats_by_category():
    """
    按类别统计
    Query: type=expense|income, from=YYYY-MM-DD, to=YYYY-MM-DD
    返回: [
      {category: "饮食", amount: 520.50, percent: 35.2, count: 15},
      ...
    ]
    按金额降序排列
    """
    # TODO: 7号实现
    pass