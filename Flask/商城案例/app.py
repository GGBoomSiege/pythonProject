from flask import Flask
from settings import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_folder='static')
app.config.from_object(MySQLConfig)
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()