# Cloud Run では gunicorn から起動されるため
# 通常はこの if __name__ == "__main__" は実行されませんが
# ローカル実行用に残しておくのが正解です

import os
from testapp import app, db   # ← 既存の Flask app を使う（作らない）

if __name__ == "__main__":
    # Cloud Run は PORT 環境変数でポートを指定してくる
    port = int(os.environ.get("PORT", 8080))

    # host=0.0.0.0 は必須（これがないと外部から見えない）
    app.run(host="0.0.0.0", port=port)
