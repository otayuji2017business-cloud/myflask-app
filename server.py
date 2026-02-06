import os
from testapp import create_app

app = create_app()

if __name__ == "__main__":
    # Cloud Run は PORT 環境変数でポートを指定してくる
    port = int(os.environ.get("PORT", 8080))

    # host=0.0.0.0 は必須（これがないと外部から見えない）
    app.run(host="0.0.0.0", port=port)
