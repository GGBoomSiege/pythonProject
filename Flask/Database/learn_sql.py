from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:operator_123456@192.168.3.234:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'opsoft'
db = SQLAlchemy(app)  # 实例化的数据库


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(32), nullable=False)
    gender = db.Column(db.Enum('男', '女'), nullable=False)
    phone = db.Column(db.String(11))

    grades = db.relationship('Grade', backref='student')
    courses = db.relationship('Course', secondary='student_to_course', backref='student')


class StudentToCourse(db.Model):
    __tablename__ = 'student_to_course'
    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(32), nullable=False)
    gender = db.Column(db.Enum('男', '女'), nullable=False)
    phone = db.Column(db.String(11))

    courses = db.relationship('Course', backref='teacher')


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)

    course_name = db.Column(db.String(32))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))

    grades = db.relationship('Grade', backref='course')


class Grade(db.Model):
    __tablename__ = 'grade'
    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    score = db.Column(db.Integer)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # db.drop_all()
