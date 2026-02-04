from testapp import app, db


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(
        host="0.0.0.0",  # どこからの通信も受ける
        port=8080,       # Cloud Run 指定ポート
        debug=False
    )

