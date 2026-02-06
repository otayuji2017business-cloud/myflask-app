from flask import render_template, request, redirect, url_for
from flask import current_app as app
from . import db
from .models import User


# -----------------------
# トップページ
# -----------------------
@app.route('/')
def index():
    user = "まる"
    age = 30
    return render_template(
        'index.html',
        user=user,
        age=age
    )


# -----------------------
# Aboutページ
# -----------------------
@app.route('/about')
def about():
    return render_template('about.html')


# -----------------------
# フォーム（登録）
# -----------------------
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')

        if not name:
            return "名前を入力してください"
        try:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"DBエラーが発生しました: {e}"

        return redirect(url_for('list_users'))

    return render_template('form.html')


# -----------------------
# ユーザー一覧
# -----------------------
@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)


# -----------------------
# 編集
# -----------------------
@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        user.name = request.form['name']
        db.session.commit()
        return redirect(url_for('list_users'))

    return render_template('edit.html', user=user)


# -----------------------
# 削除
# -----------------------
@app.route('/delete/<int:user_id>', methods=['POST'])
def delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('list_users'))
