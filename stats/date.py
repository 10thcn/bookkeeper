"""
stats/date.py — 按时间维度统计（6号）
GET /api/stats/by-date?granularity=day|week|month&from=&to=
"""

from flask import Blueprint, request, jsonify

bp = Blueprint("stats_date", __name__, url_prefix="/api/stats")


@bp.route("/by-date", methods=["GET"])
def stats_by_date():
    """
    按时间维度统计收支
    Query: granularity=day|week|month, from=YYYY-MM-DD, to=YYYY-MM-DD
    返回: [
      {period: "2026-11", income: 3500, expense: 1200, balance: 2300},
      ...
    ]
    其中 balance = income - expense
    """
    # TODO: 6号实现
    pass