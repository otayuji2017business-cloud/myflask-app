from flask import render_template, request, redirect, url_for
from . import app
from .db import save_user, get_users, delete_user, update_user, get_user

@app.route('/')
def index():
    user = "Taro"
    age = 20
    return render_template(
        'index.html',
        user=user,
        age=age
    )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sum')
def sum_page():
    a = 3
    b = 5
    total = a + b
    return render_template(
        'sum.html',
        a=a,
        b=b,
        total=total
    )

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('username')
        save_user(name)
        return redirect(url_for('list_users'))
    return render_template('form.html')


@app.route('/users')
def list_users():
    users = get_users()
    return render_template('list.html', users=users)



@app.route('/result')
def result():
    username = request.args.get('username')
    return render_template('result.html', username=username)


@app.route('/delete/<int:user_id>', methods=['POST'])
def delete(user_id):
    delete_user(user_id)
    return redirect(url_for('list_users'))

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    if request.method == 'POST':
        name = request.form.get('username')


        if not name:
            # 空なら再表示（最低限）
            user = get_user(user_id)
            error = "名前を入力してください"
            return render_template('edit.html', user=user, error=error)


        update_user(user_id, name)
        return redirect(url_for('list_users'))

    user = get_user(user_id)
    return render_template('edit.html', user=user)