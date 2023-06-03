from flask import Flask, render_template, jsonify, request, redirect, session, Blueprint
from .views.temp_1 import temp_1
from .views.temp_2 import temp_2
import functools

def create_app():
    app = Flask(__name__)
    app.register_blueprint(temp_1, url_prefix='/demo')
    app.register_blueprint(temp_2)

    app.secret_key = 'OpUser123'

    DATA_DICT = {
        '1': {'name': '张三', 'age': 18},
        '2': {'name': '李四', 'age': 18},
        '3': {'name': '王五', 'age': 18},
        '4': {'name': '赵六', 'age': 18}
    }

    def auth(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if 'username' in session:
                return func(*args, **kwargs)
            else:
                return redirect('/login')
        return inner

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'liujun' and password == 'OpUser123':
            session['username'] = 'liujun'
            return redirect('/index')
        error = '用户名或密码错误'
        return render_template('login.html', error=error)


    @app.route('/index')
    @auth
    def index():
        return render_template('user_index.html', DATA_DICT=DATA_DICT)

    @app.route('/edit/<key>', methods=['GET', 'POST'])
    @auth
    def edit(key):
        if request.method == 'GET':
            info = DATA_DICT[key]
            return render_template('edit.html', info=info)
        name = request.form.get('name')
        age = request.form.get('age')
        DATA_DICT[key]['name'] = name
        DATA_DICT[key]['age'] = age
        return redirect('/index')

    @app.route('/delete/<key>')
    @auth
    def delete(key):
        del DATA_DICT[key]
        return redirect('/index')

    return app;

if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', port=8080, debug=True)