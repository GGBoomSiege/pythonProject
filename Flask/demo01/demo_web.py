from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get/news")
def get_news():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


# @app.route('/api', methods=['post'])
# def api():
#     print(request.form.get('username'))
#     return "登陆成功"

@app.route('/api', methods=['get', 'post'])
def api():
    if request.method == 'GET':
        print(type(request.args))
        return "登陆成功"
    elif request.method == 'POST':
        print(request.form)
        return "登陆成功"
    else:
        return ('请求不支持!')


if __name__ == '__main__':
    app.run()
