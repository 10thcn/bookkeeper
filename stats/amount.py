"""
stats/amount.py — 按金额维度统计（8号）
GET /api/stats/by-amount?from=&to=
"""

from flask import Blueprint, request, jsonify

bp = Blueprint("stats_amount", __name__, url_prefix="/api/stats")


@bp.route("/by-amount", methods=["GET"])
def stats_by_amount():
    """
    金额分布统计
    Query: from=YYYY-MM-DD, to=YYYY-MM-DD
    返回: {
      count: 45,
      total: 3520.80,
      max: {id, amount, category, date},
      min: {id, amount, category, date},
      avg: 78.24,
      top5: [{...}, ...],
      distribution: [{bucket: "0-50", count: 20}, ...]
    }
    """
    # TODO: 8号实现
    pass