import os
from testapp import app, db   # ← 既存の Flask app を使う（作らない）

# ★ ここが重要：アプリ起動時にテーブル作成
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    # Cloud Run は PORT 環境変数でポートを指定してくる
    port = int(os.environ.get("PORT", 8080))

    # host=0.0.0.0 は必須（これがないと外部から見えない）
    app.run(host="0.0.0.0", port=port)
