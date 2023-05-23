from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route('/add/user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')
    username = request.form.get('username')
    password = request.form.get('password')
    mobile = request.form.get('mobile')

    sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"

    conn = pymysql.connect(host='192.168.3.234', port=3306, user='root', password='operator_123456', db='unicom', charset='utf8')

    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, [username, password, mobile])

    conn.commit()

    cursor.close()
    conn.close()

    return '添加成功'

@app.route('/show/user')
def show_user():
    sql = "select * from admin"

    conn = pymysql.connect(host='192.168.3.234', port=3306, user='root', password='operator_123456', db='unicom',
                           charset='utf8')

    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    info_lst = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('show_user.html', info_lst=info_lst)

if __name__ == '__main__':
    app.run()