from testapp import app
from testapp.db import init_db

if __name__ == '__main__':
    init_db()   # ← 初回だけDB作成
    app.run()