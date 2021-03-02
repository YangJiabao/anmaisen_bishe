import xlrd
import pymysql

#   重写插入数据方法

# def connect_db():
    # 连接数据库
db = pymysql.connect(host='localhost', user='root',
                     passwd='19971012', db='text', use_unicode=True, charset="utf8")
cur = db.cursor()

    # return db,cur


def create_library():
    # 建库建表
    # print(excel_head)
    # cols = ", ".join('{}'.format(k) for k in excel_head)
    # cur.execute("create database AMS character set utf8;")
    # CREATE DATABASE IF NOT EXISTS RUNOOB DEFAULT CHARSET utf8 COLLATE utf8_general_ci;. 如果数据库不存在则创建，存在则不创建。创建RUNOOB数据库，并设定编码集为utf8
    # 建表
    sql = """
          create table test_an1(
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
    cur.execute(sql)
    db.close()


def inquire_db(number1):
    # 查询数据库
    db.ping(reconnect=True)
    cur.execute("SELECT * FROM test_an1 WHERE 商品编号 = '%s'" % number1 )
    # cur.execute("SELECT * FROM an;")
    info = cur.fetchall()
    print(info)
    print(number1)
    for d in info:
        print("编号为：" + list(d)[1])
        print("数量为：" + list(d)[9])#当前数量
    return number1

    # print(type(info))
    # for row, head in zip(info, range(len(excel_head))):
    #     excel_head[head] = row[head]
    #     fname = row[0]
    #     lname = row[1]
    #     age = row[2]
    #     sex = row[3]
    #     income = row[4]
    #     # 打印结果
    #     print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
    #           (fname, lname, age, sex, income))


def change_db(serial_number, quantity):
    db.ping(reconnect=True)#ping数据库是否关闭，关闭就打开
    sql = "update test_an1 set 物料编码 = 物料编码 + %s where 商品编号 = '%s'" %(serial_number, quantity)
    print(sql)
    cur.execute(sql)
    db.commit()
    db.close()


def insert_db(data):#, cols, val_cols
    db.ping(reconnect=True)
    print(data)
    # serial_number = "C154876"
    # info = cur.fetchall()
    # if info == ():
    #     print(111)
    # print(info)
    pop = []
    for i in range(len(data)):
        db.ping(reconnect=True)
        print(data[i][1] + "-" + data[i][9]+ "-" + str(i))
        cur.execute("SELECT * FROM test_an1 WHERE 商品编号 = '%s'" % data[i][1])
        info = cur.fetchall()
        if info != ():
            print('QAQ！数据已存在啦，'+ data[i][1] +'已经增加数量'+ data[i][9] +'了哦！')
            change_db(data[i][9], data[i][1])
            print(data[i])
            pop.append(data[i])
    # print(pop)
    for i in range(len(pop)):
        # print(pop[i])
        data.remove(pop[i])
    print(data)
        # serial_number.append(data[i][1])
    # sql = "SELECT * FROM test_an1 WHERE 商品编号 = '%s'"
    # cur.executemany(sql, serial_number)
        # change_db(inquire_db(data[i][1]), data[i][9])
    # print(data)
    # 插入数据
    try:
        db.ping(reconnect=True)  # ping数据库是否关闭，关闭就打开
        sql = "insert into test_an1(`购买类型`, `商品编号`, `物料编码`, `商品分类`, `名称`, `商品型号`, `品牌`, `封装规格`, `单个毛重`, `购买数量`, `商品单价`, `金额`) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # res_sql = sql % (cols, val_cols)
        # print(res_sql)  # 'insert into users(`name`, `age`) values(%(name)s, %(age)s)'
        cur.executemany(sql, data)  # 批量化插入  列表   列表里必须是元组
        # cursor.executemany('insert into weibo values( %s,  %s, %s)'
        db.commit()  # 提交到数据库执行
        print("OAO！新字段插入成功啦！")
        # 关闭数据库连接
        db.close()
    except:
        print("QAQ！没有新字段需要插入呜呜呜呜~~！")



def get_excel(address):
    # 打开文件,默认打开第一个sheet
    workbook = xlrd.open_workbook(address)
    # sheet1,索引是从0开始,得到sheet1表的句柄.用这个可以操作表
    sheet1 = workbook.sheet_by_index(1)
    # # 表名
    # print(sheet1.name)
    # # 有效行数
    # print(sheet1.nrows)
    # # 有效列数
    # print(sheet1.ncols)
    # return sheet1

# def read_excel_head(sheet1):
#     #得到Excel的表头词条
#     excel_head = sheet1.row_values(1)
#     # 循环得到sheet1表的内容
#     # print(excel_head)
#     return excel_head

# def formatting_list():
    #格式化数据
    data_list = []
    for i in range(2, sheet1.nrows - 1):#循环行数
        dict = []
        # row_values = sheet1.row_values(i)
        # print(sheet1.row_values(i))#获取行数据
        for j in range(sheet1.ncols):#循环列数
            # dict[excel_head[j]] = sheet1.row_values(i)[j]
            dict.append(sheet1.row_values(i)[j])
        data_list.append(tuple(dict))
        # print(tuple(dict))
    # print( sheet1.nrows)
    print(data_list)
    # print(len(data_list))
    # for i in range(len(data_list)):
    #     print(data_list[i][1] + "-" + data_list[i][9]+ "-" + str(i))
    #     change_db(inquire_db(data_list[i][1]), data_list[i][9])
    return data_list




if __name__ == '__main__':
    # sheet1 = get_excel(r'1.xls')
    # excel_head = read_excel_head(sheet1)
    data_list = get_excel(r'1.xls')
    # db, cur = connect_db()
    # create_library()      #建库建表
    # insert_db(data_list)      #插入数据
    # number = 'C251614'
    # inquire_db(number)      #查数据（未完善）
    # quantity = 2      #需要增加的数量
    # serial_number = 'C235378'     #需要增加数量的型号
    # change_db(quantity, serial_number)      #修改数据库数据
