import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db は先に作る（appはまだ渡さない）
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # =====================
    # 基本設定
    # =====================
    app.config['SECRET_KEY'] = 'dev-secret-key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # =====================
    # Cloud SQL 設定
    # =====================
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_NAME = os.environ.get("DB_NAME")
    INSTANCE_CONNECTION_NAME = os.environ.get("INSTANCE_CONNECTION_NAME")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@/"
        f"{DB_NAME}?host=/cloudsql/{INSTANCE_CONNECTION_NAME}"
    )

    # =====================
    # DB 初期化（ここで初めて接続）
    # =====================
    db.init_app(app)

    # =====================
    # ルーティング・モデル読込
    # =====================
    with app.app_context():
        from . import views, models
        db.create_all()

    return app
