import pymysql

conn = pymysql.connect(host='192.168.3.234', port=3306, user='root', password='operator_123456', db='unicom',
                       charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
#
# cursor.execute(sql, ['刘俊', 'admin', '12345678910'])
#
# sql = "insert into admin(username,password,mobile) values(%(n1)s,%(n2)s,%(n3)s)"
#
# cursor.execute(sql, {'n1':"刘俊1", 'n2':"admin", 'n3':"12345678910"})
#
# conn.commit()

sql = "select * from admin where id > %s"
cursor.execute(sql,[2])
data_list = cursor.fetchall()

print(data_list)

cursor.close()
conn.close()
