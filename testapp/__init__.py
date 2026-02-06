

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
# Cloud Run では永続化されないが、今はOK
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mysql+pymysql://flaskuser:PASSWORD@/myflaskdb"
    "?unix_socket=/cloudsql/PROJECT_ID:asia-northeast1:INSTANCE_NAME"
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
