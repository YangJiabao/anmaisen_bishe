print("%(name)s  %(age)s" % ({'name': ['Lihua','sds'], 'age': [20,10]}))
import pymysql
import json
levelname = 'haha'
name = 'xixi'
message = 'kexuan'

BASIC_FORMAT = "%(levelname)s    %(name)s    %(message)s"
print (BASIC_FORMAT % { 'name': name,'levelname': levelname, 'message': message})


# a = ['qwe','qwe',dasd]
# a = ['购买类型', '商品编号', '物料编码', '商品分类', '名称', '商品型号', '品牌', '封装规格', '单个毛重', '购买数量', '商品单价', '金额']
# cols = ", ".join('{}'.format(k) for k in a)
# print([cols])



# def insert_db(data):#, cols, val_cols
#     # 建库和建表
db = pymysql.connect(host='localhost', user='root',
                     passwd='19971012', db='text', use_unicode=True, charset="utf8")
cur = db.cursor()
# data = [{'id':[1, 2, 3]},{'user_id': [4, 5, 6]}, {'`name`':[7, 8, 9]}]
# data = [(1, 2, 3)]
# data = [{'id':[1, 2, 3], 'user_id': [4, 5, 6], '`name`':[7, 8, 9]}]
# sql = "insert into test_an(`'购买类型'`, `'商品编号'`, `'物料编码'`, `'商品分类'`, `'名称'`, `'商品型号'`, `'品牌'`, `'封装规格'`, `'单个毛重'`, `'购买数量'`, `'商品单价'`, `'金额'`) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# sql = "insert into test_an(id, user_id, `name`) values(%(id)s, %(user_id)s, %(`name`)s)"
# sql = "insert into test_an(user_id, id, `name`) values(%s, %s, %s)"
# res_sql = sql % (cols, val_cols)
# print(res_sql)  # 'insert into users(`name`, `age`) values(%(name)s, %(age)s)'
# cur.executemany(sql.replace('\'',''), data)  # 批量化插入  列表   列表里必须是元组
# cursor.executemany('insert into weibo values( %s,  %s, %s)'

# db.commit()  # 提交到数据库执行
    # # 关闭数据库连接
    # db.close()


# cur.execute("select user from mysql.user")
# # info = cur.fetchall()
# b = cur.fetchall()
# for i in b:
#     print(i[0])


# sql = "create user {}@'%' identified by ''".format('qwer')
# cur.execute(sql)
sql = "drop user '1234'"
cur.execute(sql)


# def inquire_db():
#     # 查询数据库
#     db.ping(reconnect=True)
#     cur.execute("SELECT * FROM test_an1 WHERE 商品编号 = '%s'" % 'c251614')
#     info = cur.fetchall()
#     print(info)
# inquire_db()





# data = [(1,2,3,4,5,6,7,8,9,0,11,12),(1,2,3,4,5,6,7,8,9,0,11,12),(1,2,3,4,5,6,7,8,9,0,11,12),(1,2,3,4,5,6,7,8,9,0,11,12),(1,2,3,4,5,6,7,8,9,0,11,12),(1,2,3,4,5,6,7,8,9,0,11,12),(1,2,3,4,5,6,7,8,9,0,11,12),(1,2,3,4,5,6,7,8,9,0,11,12),(1,2,3,4,5,6,7,8,9,0,11,12),(1,2,3,4,5,6,7,8,9,0,11,12),(1,2,3,4,5,6,7,8,9,0,11,12),(1,2,3,4,5,6,7,8,9,0,11,12)]
# data = [(1,'',3,4,5,6,7,8,9,0,11,12)]
# data = [(1),(1),(1),(1),(1),(1),(1),(1),(1),(1),(1),(1)]
# insert_db(data)


#
# a = (购买类型, '购买类型', '购买类型', '购买类型', '购买类型', '购买类型', '购买类型')
# print(a)

# excel_head = ['购买类型', '商品编号', '物料编码', '商品分类', '名称', '商品型号', '品牌', '封装规格', '单个毛重', '购买数量', '商品单价', '金额']
# excel_head = ['sad', 'sda', 'dd', 'ww', 'dw', 'aw', 'ddf', 'er', 'tr', 'fg', 'hh', 'gb']
# db = pymysql.connect(host='localhost', user='root',
#                          passwd='19971012', db='text', use_unicode=True, charset="utf8")
# cur = db.cursor()
#

# sql = """
#           create table if not EXISTS %s(
#               购买类型 varchar(255),
#               商品编号 varchar(255),
#               物料编码 varchar(255),
#               商品分类 varchar(255),
#               名称 varchar(255),
#               商品型号 varchar(255),
#               品牌 varchar(255),
#               封装规格 varchar(255),
#               单个毛重 varchar(255),
#               购买数量 varchar(255),
#               商品单价 varchar(255),
#               金额 varchar(255))
#           """ % ('text')
#     # sql = "insert into an(`购买类型`, `商品编号`, `物料编码`, `商品分类`, `名称`, `商品型号`, `品牌`, `封装规格`, `单个毛重`, `购买数量`, `商品单价`, `金额`) values('14', '23', '23', '43', '324', '543', '342', '45345', '45342', '234', '2342', '23423')"
#     # sql = """update an set 物料编码 = 666"""
# cur.execute(sql)
# except:
#     print("cunzai")
# db.commit()
# db.close()


# print(d)


# try:
#     db = pymysql.connect(host='localhost', user='root1',
#                          passwd='19971012', db='text', use_unicode=True, charset="utf8")
#     cur = db.cursor()
#     # 处理异常程序不退出----另做一个函数，用于控制整个程序的走向，如果异常就重新执行连接函数，直到没有异常继续向下执行，类似if __name__ == '__main__':，主控函数-----重新获取用户名密码
# except :
#     print("失败")


# print("输入：")
# a = input()
# while True:
#     if a != '4':
#         print("对了")
#         break
#     else:
#         print("输入：")
#         a = input()




# a = [(1,2),(3,4)]
# a.pop(1)
# print(a)









# from PyQt5 import QtCore, QtGui, QtWidgets
#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(549, 199)
#         self.user_label = QtWidgets.QLabel(Form)
#         self.user_label.setGeometry(QtCore.QRect(50, 40, 61, 21))
#         self.user_label.setObjectName("user_label")
#         self.user_lineEdit = QtWidgets.QLineEdit(Form)
#         self.user_lineEdit.setGeometry(QtCore.QRect(130, 40, 113, 20))
#         self.user_lineEdit.setObjectName("user_lineEdit")
#         self.pwd_label = QtWidgets.QLabel(Form)
#         self.pwd_label.setGeometry(QtCore.QRect(50, 80, 54, 12))
#         self.pwd_label.setObjectName("pwd_label")
#         self.pwd_lineEdit = QtWidgets.QLineEdit(Form)
#         self.pwd_lineEdit.setGeometry(QtCore.QRect(130, 70, 113, 20))
#         self.pwd_lineEdit.setObjectName("pwd_lineEdit")
#         self.login_Button = QtWidgets.QPushButton(Form)
#         self.login_Button.setGeometry(QtCore.QRect(50, 110, 75, 23))
#         self.login_Button.setObjectName("login_Button")
#         self.cancel_Button = QtWidgets.QPushButton(Form)
#         self.cancel_Button.setGeometry(QtCore.QRect(160, 110, 75, 23))
#         self.cancel_Button.setObjectName("cancel_Button")
#         self.user_textBrowser = QtWidgets.QTextBrowser(Form)
#         self.user_textBrowser.setGeometry(QtCore.QRect(270, 30, 221, 101))
#         self.user_textBrowser.setObjectName("user_textBrowser")
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "用户登录"))
#         self.user_label.setText(_translate("Form", "用户名"))
#         self.pwd_label.setText(_translate("Form", "密码"))
#         self.login_Button.setText(_translate("Form", "登录"))
#         self.cancel_Button.setText(_translate("Form", "退出"))





