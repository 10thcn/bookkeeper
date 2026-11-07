"""
个人记账本 — Flask 应用入口（1号·组长）
负责：工厂函数、蓝图注册、静态文件托管、全局错误处理
"""
from flask import Flask, send_from_directory
import os


def create_app():
    """Flask 应用工厂"""
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")

    # ── 确保数据目录存在 ──
    os.makedirs(os.path.join(app.root_path, "data"), exist_ok=True)

    # ── 注册蓝图 ──
    from routes.records import bp as records_bp
    from routes.query import bp as query_bp
    from routes.io import bp as io_bp
    from stats.date import bp as stats_date_bp
    from stats.category import bp as stats_category_bp
    from stats.amount import bp as stats_amount_bp

    app.register_blueprint(records_bp)
    app.register_blueprint(query_bp)
    app.register_blueprint(io_bp)
    app.register_blueprint(stats_date_bp)
    app.register_blueprint(stats_category_bp)
    app.register_blueprint(stats_amount_bp)

    # ── 全局错误处理 ──
    @app.errorhandler(404)
    def not_found(e):
        return {"ok": False, "errors": ["资源不存在"]}, 404

    @app.errorhandler(500)
    def server_error(e):
        return {"ok": False, "errors": ["服务器内部错误"]}, 500

    # ── 前端入口 ──
    @app.route("/")
    def index():
        return send_from_directory("templates", "index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)