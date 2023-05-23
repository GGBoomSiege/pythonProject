#mysql settings
class MySQLConfig(object):

    DEBUGE = True
    SECRET_KEY = "OpUser123"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{ipaddress}:{port}/{database}".format(username="root",password="operator_123456",ipaddress="192.168.3.234",port="3306",database="mall")
    SQLALCHEMY_TRACK_MODIFICATIONS = True #动态追踪修改设置
    SQLALCHEMY_ECHO = True