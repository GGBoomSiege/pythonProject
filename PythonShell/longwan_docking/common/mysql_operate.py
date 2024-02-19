import pymysql
from config.setting import *

class MysqlDb():
    def __init__(self, host, port, user, passwd, db):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            autocommit=True
        )
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def insert(self, tbname, params):
        lists = [(k, params[k]) for k in params if params[k]]
        sentence = 'insert into %s (' % tbname + ','.join([i[0] for i in lists]) + ') values (' + ','.join(
            ['%r' % i[1] for i in lists]) + ');'
        sentence = sentence.replace("'None'","NULL")
        sentence = sentence.replace('"None"', "NULL")
        self.conn.ping(reconnect=True)
        self.cur.execute(sentence)

    def select_all(self, sql):
        """ 返回全部记录 """
        self.conn.ping(reconnect=True)
        sql = sql.replace("='None'", " is NULL")
        sql = sql.replace('="None"', " is NULL")
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def select_one(self, sql):
        """ 返回单记录 """
        self.conn.ping(reconnect=True)
        sql = sql.replace("='None'", " is NULL")
        sql = sql.replace('="None"', " is NULL")
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def execute_db(self, sql):
        """更新/新增/删除"""
        if sql.startswith("update"):
            sql = sql.replace("'None'", "NULL")
            sql = sql.replace('"None"', "NULL")
        else:
            sql = sql.replace("='None'", " is NULL")
            sql = sql.replace('="None"', " is NULL")

        print(sql)
        try:
            self.conn.ping(reconnect=True)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("操作出现错误：{}".format(e))
            self.conn.rollback()


    def update(self, tbname, params, condition=None):
        """ 更新 """
        self.conn.ping(reconnect=True)
        update_list = self._deal_values(params)
        update_data = ",".join(update_list)
        if condition:
            sentence = "update {table} set {values} where {condition}".format(table=tbname, values=update_data,
                                                                              condition=condition)
        else:
            sentence = "update {table} set {values}".format(table=tbname, values=update_data)
        sentence = sentence.replace("None", "NULL")
        self.cur.execute(sentence)

    def _deal_values(self, value):
        """
        self._deal_values(value) -> str or list
            处理传进来的参数

        """
        # 如果是字符串则加上''
        if isinstance(value, str):
            value = value.replace("'", "\\'")
            value = ("'{value}'".format(value=value))
        # 如果是字典则变成key=value形式
        elif isinstance(value, dict):
            result = []
            for key, value in value.items():
                value = self._deal_values(value)
                res = "{key}={value}".format(key=key, value=value)
                result.append(res)
            return result
        else:
            value = (str(value))
        return value

dbo_cdb = MysqlDb(MYSQL_CHOST, MYSQL_CPORT, MYSQL_CUSER, MYSQL_CPASSWD, MYSQL_CDB)
