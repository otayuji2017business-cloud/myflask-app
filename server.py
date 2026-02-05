from testapp import app, db
import os
from flask import Flask

# Flask アプリを作成
app = Flask(__name__)

# ルート（ / ）にアクセスしたときの処理
@app.route("/")
def index():
    return "Hello from Cloud Run!"

# Cloud Run では gunicorn から起動されるため
# 通常はこの if __name__ == "__main__" は実行されませんが
# ローカル実行用に残しておくのが正解です
if __name__ == "__main__":
    # Cloud Run は PORT 環境変数でポートを指定してくる
    port = int(os.environ.get("PORT", 8080))

    # host=0.0.0.0 は必須（これがないと外部から見えない）
    app.run(host="0.0.0.0", port=port)
