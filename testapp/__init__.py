
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask アプリを作成（★ここで1回だけ）
app = Flask(__name__)

# =====================
# アプリ設定
# =====================
# app.config.from_object('testapp.config') # 今は無効化しておく

# SECRET_KEY（Flask必須。簡易でOK）
app.config['SECRET_KEY'] = 'dev-secret-key'


# SQLite（学習用）→cloud SQLを入れます。
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


# SQLAlchemyの警告を抑制
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# =====================
# DB 初期化
# =====================
db = SQLAlchemy(app)


# =====================
# ルーティング・モデル読込
# =====================
# app と db を定義した「後」で import するのが重要
from . import views, models
