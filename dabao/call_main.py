# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
import pymysql
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
#导入designer工具生成的login模块
from ui import Ui_MainWindow
import os
from warnings import filterwarnings
import xlrd

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        filterwarnings("error", category=pymysql.Warning)                        #  指定过滤告警的类别为 pymysql.Warning类，
        self.actionV0_0_1.triggered.connect(self.author)                         #  绑定关于作者
        self.lineEdit.setText('root')                                            #  预设用户名
        self.lineEdit_2.setText('19971012')                                      #  预设密码
        self.pushButton.clicked.connect(self.connect_db)                         #  绑定连接数据库按钮信号槽
        # self.pushButton_2.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.open_file)                        #  绑定打开文件（选择文件按钮）信号槽
        self.actionCreate_a_table.triggered.connect(self.create_table)           #  绑定开始-创建表
        self.actionCreate_a_database.triggered.connect(self.create_database)     #  绑定开始-创建库
        self.pushButton_3.clicked.connect(self.insert_db)                        #  绑定插入数据库（导入按钮）信号槽
        self.pushButton_7.clicked.connect(self.change_db_out)                    #  绑定批量导出数据库（导出按钮）信号槽
        self.pushButton_4.clicked.connect(self.inquire_db)                       #  绑定查询数据库（按照编号查询按钮）信号槽
        self.pushButton_5.clicked.connect(self.change_db_add)                    #  绑定入库按钮信号槽
        self.pushButton_6.clicked.connect(self.change_db_shear)                  #  绑定出库按钮信号槽

    def connect_db(self):
        # 连接数据库
        flag = 1  # 设置一个判断程序有没有走异常处理的标识
        try:
            # username = self.lineEdit.text()
            # password = self.lineEdit_2.text()
            # global db
            self.db = pymysql.connect(host='localhost', user=self.lineEdit.text(),
                                 passwd=self.lineEdit_2.text(), db='text', use_unicode=True, charset="utf8")
            self.textBrowser.append("OAO！太棒了！连接成功了！")
            # global cur
            self.cur = self.db.cursor()
        except:
            flag = 0
            self.textBrowser.append("QAQ！连接出错了呀，检查一下用户名密码哦~~~")
            self.pushButton.disconnect()#断开信号的连接，保证不会一直跑异常，使程序进入等待页面
            self.lineEdit.clear()
            self.lineEdit_2.clear()
        if flag == 0:
            self.pushButton.clicked.connect(self.connect_db)          #重新打开信号的连接，确保按钮依然有用

    def create_database(self):
        #建库
        try:
            try:
                self.cur.execute("CREATE DATABASE IF NOT EXISTS text DEFAULT CHARSET utf8 COLLATE utf8_general_ci;") #如果数据库不存在则创建，存在则不创建。创建RUNOOB数据库，并设定编码集为utf8
                self.textBrowser.append("OAO！PERFECT！库已创建好了！")
            except pymysql.Warning as e:
                self.textBrowser.append("QAQ！数据库已经创建过了哦！")
        except:
            self.textBrowser.append("QAQ！数据库还没连接，别着急先登录一下数据库哦！")

    def create_table(self):
        # 建表
        # print(excel_head)
        flag = 1    #  设置一个判断程序有没有走异常处理的标识
        # cols = ", ".join('{}'.format(k) for k in excel_head)
        # cur.execute("create database AMS character set utf8;")
        # CREATE DATABASE IF NOT EXISTS RUNOOB DEFAULT CHARSET utf8 COLLATE utf8_general_ci;. 如果数据库不存在则创建，存在则不创建。创建RUNOOB数据库，并设定编码集为utf8
        # 建表
        try:
            self.db.ping(reconnect=True)  # ping数据库是否关闭，关闭就打开
            sql = """
                  create table if not EXISTS test_an1(
                      购买类型 varchar(255),
                      商品编号 varchar(255),
                      物料编码 varchar(255),
                      商品分类 varchar(255),
                      名称 varchar(255),
                      商品型号 varchar(255),
                      品牌 varchar(255),
                      封装规格 varchar(255),
                      单个毛重 varchar(255),
                      购买数量 varchar(255),
                      商品单价 varchar(255),
                      金额 varchar(255))
                  """
            try:
                self.cur.execute(sql)
                self.textBrowser.append("OAO！NICE！表已创建好了！")
            except pymysql.Warning as e:
                self.textBrowser.append("QAQ！表已经存在了！")
            self.db.close()
        except:
            flag = 0
            self.textBrowser.append("QAQ！数据库还没连接，别着急先登录一下数据库哦！")
            self.actionCreate_a_table.disconnect()
        if flag == 0 :
            self.actionCreate_a_table.triggered.connect(self.create_table)


    def open_file(self):
        #打开文件选择窗口并格式化数据
        try:
            fileName,fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
            "XLS Files(*.xls)")
            # print(fileName)
            # print(fileType)
            self.textBrowser_2.setText(fileName)
            # self.address = fileName
            # return fileName
            # 打开文件,默认打开第一个sheet
            workbook = xlrd.open_workbook(fileName)
            # sheet1,索引是从0开始,得到sheet1表的句柄.用这个可以操作表
            sheet1 = workbook.sheet_by_index(1)
            flag = 1  # 标记默认是格式化入库数据
            flag_index = 2  # 标记出库数量所在的Excel下标
            self.excel_head = sheet1.row_values(1)  # 得到Excel的表头词条
            for j in range(len(self.excel_head)):
                if self.excel_head[j] == '出库数量':
                    # print('222')
                    flag = 0  # 有出库数量则改为0  标记为格式化出库数据
                    flag_index = j  # 标记下标
                if self.excel_head[j] == '购买数量':
                    self.numb_index = j
                if self.excel_head[j] == '商品编号':
                    self.commodity_index = j
            # 格式化数据
            if flag == 1:
                self.textBrowser.append('OAO！是入库文件哦~~~~')
                self.data_list = []
                for i in range(2, sheet1.nrows - 1):  # 循环行数
                    dict = []
                    # row_values = sheet1.row_values(i)
                    # print(sheet1.row_values(i))#获取行数据
                    for j in range(sheet1.ncols):  # 循环列数
                        # dict[excel_head[j]] = sheet1.row_values(i)[j]
                        dict.append(sheet1.row_values(i)[j])
                    self.data_list.append(tuple(dict))
                    # print(tuple(dict))
                # print(self.data_list)
            # return data_list
            else:
                # print('出库')
                self.textBrowser.append('QAQ！是出库文件啊~~~~')
                self.data_list = []
                self.numb_list = []
                for i in range(2, sheet1.nrows - 1):  # 循环行数
                    # dict = []
                    # print(sheet1.row_values(i)[flag_index])#获取行数据
                    # dict.append(str(sheet1.row_values(i)[flag_index]))
                    # print(dict)
                    self.data_list.append(str(int(sheet1.row_values(i)[flag_index])))
                    self.numb_list.append(sheet1.row_values(i)[self.commodity_index])
                # print(data_list)
                # print(numb_list)
                # self.change_db_out(numb_list, data_list)
        except:
            self.textBrowser.append("QAQ！没有打开文件哦~~~")

    def change_db_add(self):  #  数量   编号
        try:
            if self.lineEdit_5.text() == '' or self.lineEdit_3.text() == '':
                self.textBrowser.append("QAQ！要正确填写编号和数量哦~~~")
            else:
                self.db.ping(reconnect=True)  # ping数据库是否关闭，关闭就打开
                sql = "update test_an1 set 购买数量 = 购买数量 + %s where 商品编号 = '%s'" % (self.lineEdit_5.text(), self.lineEdit_3.text())
                self.cur.execute(sql)
                self.db.commit()
                self.textBrowser.append("OAO！入库成功了呀~~~")
                self.db.close()
        except:
            self.textBrowser.append("QAQ！数据库还没连接啊~~~")
    def change_db_shear(self):  #  数量   编号
        try:
            if self.lineEdit_5.text() == '' or self.lineEdit_3.text() == '':
                self.textBrowser.append("QAQ！要正确填写编号和数量哦~~~")
            else:
                self.db.ping(reconnect=True)  # ping数据库是否关闭，关闭就打开
                sql = "update test_an1 set 购买数量 = 购买数量 - '%s' where 商品编号 = '%s'" % (self.lineEdit_5.text(), self.lineEdit_3.text())
                self.cur.execute(sql)
                self.db.commit()
                self.textBrowser.append("QAQ！出库成功了呀~~~")
                self.db.close()
        except:
            self.textBrowser.append("QAQ！数据库还没连接啊~~~")

    def change_db_out(self):  # numb  商品编号list   count   出库数量list    # self.change_db_out(numb_list, data_list)
        try:
            for numb1, count1 in zip(self.numb_list, self.data_list):
                # reality_numb = inquire_db(numb1)  # 调用查询函数查询 当前型号 在库中的实际数量
                reality_numb = 1
                self.db.ping(reconnect=True)
                self.cur.execute("SELECT * FROM test_an1 WHERE 商品编号 = '%s'" % numb1)
                info = self.cur.fetchall()
                # print(info)
                if info != ():
                    for d in info:
                        # self.textBrowser.append("编号为：" + list(d)[1] + "  数量为：" + list(d)[9])
                        reality_numb = list(d)[self.numb_index]
                residue_count = int(reality_numb) - int(count1)  # 利用实时数量减去需要出库的数量  得出剩余数量
                if residue_count >= 0:  # 判断剩余数量  如果大于0  这出库，小于  0   则提醒库存不足
                    self.db.ping(reconnect=True)  # ping数据库是否关闭，关闭就打开
                    sql = "update test_an1 set 购买数量 = 购买数量 - %s where 商品编号 = '%s'" % (count1, numb1)
                    # print(sql)
                    self.cur.execute(sql)
                    self.db.commit()
                    self.textBrowser.append(numb1 + ' 型号出库成功~~~ 出库数量：'+ count1 +' 出库后数量为：' + str(residue_count))
                    QApplication.processEvents()  # 实时刷新命令因为  textBrowser.append 它是等到此程序运行完了以后再刷新，很影响美观。
                    self.db.close()
                else:
                    self.textBrowser.append(numb1 + ' 型号库存不够啦~  当前库存为：' + str(reality_numb) + ' 需要出库数量为：' + count1)
        except:
            self.textBrowser.append("QAQ！检查一下登录和文件哦~~~~")

    def inquire_db(self):
        # 查询数据库
        try:
            self.db.ping(reconnect=True)
            self.cur.execute("SELECT * FROM test_an1 WHERE 商品编号 = '%s'" % self.lineEdit_3.text())
            info = self.cur.fetchall()
            # print(info)
            if info != ():
                for d in info:
                    self.textBrowser.append("编号为：" + list(d)[self.commodity_index] + "  数量为：" + list(d)[self.numb_index])
                    # print("编号为：" + list(d)[1])
                    # print("数量为：" + list(d)[9])  # 当前数量
            else:
                self.textBrowser.append("没找到哦~~~编号是正确的吗？")
            # self.lineEdit_3.clear()
        except:
            self.textBrowser.append("QAQ！数据库连接了吗？")

    def insert_db(self):  # , cols, val_cols
        # self.db.ping(reconnect=True)
        # print(self.data_list)
        self.textBrowser.append("QAQ！稍等一下哦~~~~")
        QApplication.processEvents()  # 实时刷新命令因为  textBrowser.append 它是等到此程序运行完了以后再刷新，很影响美观。
        try:
            pop = []
            for i in range(len(self.data_list)):
                self.db.ping(reconnect=True)
                # print(self.data_list[i][1] + "-" + self.data_list[i][9] + "-" + str(i))
                self.cur.execute("SELECT * FROM test_an1 WHERE 商品编号 = '%s'" % self.data_list[i][self.commodity_index])
                info = self.cur.fetchall()
                if info != ():
                    # print('QAQ！数据已存在啦，已经修改数量了哦！')
                    self.textBrowser.append("QAQ！数据已存在啦，"+ self.data_list[i][self.commodity_index] +"已经增加数量"+ self.data_list[i][self.numb_index] +"了哦！")
                    QApplication.processEvents()   #  实时刷新命令因为  textBrowser.append 它是等到此程序运行完了以后再刷新，很影响美观。
                    # self.change_db(self.data_list[i][9], self.data_list[i][1])
                    sql = "update test_an1 set 购买数量 = 购买数量 + %s where 商品编号 = '%s'" % (self.data_list[i][self.numb_index], self.data_list[i][self.commodity_index])
                    self.cur.execute(sql)
                    self.db.commit()
                    pop.append(self.data_list[i])
            # print(pop)
            for i in range(len(pop)):
                # print(pop[i])
                self.data_list.remove(pop[i])
            # print(self.data_list)
            try:
                self.db.ping(reconnect=True)  # ping数据库是否关闭，关闭就打开
                # sql = "insert into test_an1(`购买类型`, `商品编号`, `物料编码`, `商品分类`, `名称`, `商品型号`, `品牌`, `封装规格`, `单个毛重`, `购买数量`, `商品单价`, `金额`) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cols = ", ".join('`{}`'.format(k) for k in self.excel_head)
                val_cols = ', '.join('%s'.format(k) for k in self.excel_head)
                sql = "insert into test_an1(%s) values(%s)"
                res_sql = sql % (cols, val_cols)
                # print(res_sql)  # 'insert into users(`name`, `age`) values(%(name)s, %(age)s)'
                self.cur.executemany(res_sql.replace('\'',''), self.data_list)  # 批量化插入  列表   列表里必须是元组
                # cursor.executemany('insert into weibo values( %s,  %s, %s)'
                self.db.commit()  # 提交到数据库执行
                # print("OAO！新字段插入成功啦！")
                self.textBrowser.append("OAO！字段插入成功啦！")
                # 关闭数据库连接
                self.db.close()
            except:
                # print("QAQ！没有新字段需要插入呜呜呜呜~~！")
                self.textBrowser.append("QAQ！没有新字段需要插入呜呜呜呜~~！")
        except:
            self.textBrowser.append("QAQ！检查一下登录和文件哦~~~~")
    def author(self):
        self.textBrowser.append("既然你诚心诚意的点击了，我便大发慈悲的告诉你，为了防止世界被破坏，为了维护世界的和平，贯彻爱与真实的邪恶，可爱又迷人的反派角色，小安~~~小杨~~~，我们是穿梭在AMS的捣蛋队，白洞，白色的明天在等着我们，就是这样 ~~~~~喵~~~~~喵~~~~~   (掌声~~~)(掌声~~~)(掌声~~~)")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())