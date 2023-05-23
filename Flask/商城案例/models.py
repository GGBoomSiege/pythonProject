from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    account = db.Column(db.String(11), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    avatar = db.Column(db.String(256), nullable=False)
    age = db.Column(db.Integer)
    idCard = db.Column(db.String(18), nullable=False)
    gender = db.Column(db.Enum('男', '女'), nullable=False)
    createTime = db.Column(db.DateTime)
    loginTime = db.Column(db.DateTime)
    logoutTime = db.Column(db.DateTime)
    balance = db.Column(db.Float(10))
    court = db.relationship('Court')

    def __repr__(self):
        return '<User:%S' % self.name


class Court(db.Model):
    __tablename__ = 'court'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user._id'))
    user = db.relationship('User')
    number = db.Column(db.Integer, default=0)

    def __repr__(self):
        return 'Court:%s' % self.number


class Address(db.Model):
    __tablename__ = 'address'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    _id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user._id'))
    address = db.relationship('Address',backref='User',lazy='dynamic')
    idCard = db.Column(db.String(18))
    idCard = db.Column(db.String(18))
    idCard = db.Column(db.String(18))
    idCard = db.Column(db.String(18))

    def __repr__(self):
        return '<Court:%S' % self.name
