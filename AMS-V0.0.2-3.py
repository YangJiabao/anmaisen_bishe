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
    number = 1
    for d in info:
        print("编号为：" + list(d)[1])
        print("数量为：" + list(d)[9])#当前数量
        number = list(d)[9]
    return number

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


def insert_db(data, eh):#, cols, val_cols
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
            print(i)
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
    # try:
    db.ping(reconnect=True)  # ping数据库是否关闭，关闭就打开
    # sql = "insert into test_an1(`购买类型`, `商品编号`, `物料编码`, `商品分类`, `名称`, `商品型号`, `品牌`, `封装规格`, `单个毛重`, `购买数量`, `商品单价`, `金额`) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # res_sql = sql % (cols, val_cols)

    cols = ", ".join('`{}`'.format(k) for k in eh)
    print(cols)  # '`name`, `age`'
    # cols = '`时间`, `来自`, `内容`'
    # val_cols = ', '.join('%({})s'.format(k) for k in formatting_chars.keys())
    val_cols = ', '.join('%s'.format(k) for k in eh)
    print(val_cols)  # '%(name)s, %(age)s'
    sql = "insert into test_an1(%s) values(%s)"
    res_sql = sql % (cols, val_cols)
    print(res_sql)

    # print(res_sql)  # 'insert into users(`name`, `age`) values(%(name)s, %(age)s)'
    cur.executemany(res_sql.replace('\'',''), data)  # 批量化插入  列表   列表里必须是元组
    # cursor.executemany('insert into weibo values( %s,  %s, %s)'
    db.commit()  # 提交到数据库执行
    print("OAO！新字段插入成功啦！")
    # 关闭数据库连接
    db.close()
    # except:
    #     print("QAQ！没有新字段需要插入呜呜呜呜~~！")

def change_db_out(numb, count):  #  numb  商品编号list   count   出库数量list
    for numb1, count1 in zip(numb, count):
        reality_numb = inquire_db(numb1)   #  调用查询函数查询 当前型号 在库中的实际数量
        residue_count = int(reality_numb) - int(count1)   #  利用实时数量减去需要出库的数量  得出剩余数量
        if residue_count >= 0:       #  判断剩余数量  如果大于0  这出库，小于  0   则提醒库存不足
            db.ping(reconnect=True)  # ping数据库是否关闭，关闭就打开
            sql = "update test_an1 set 物料编码 = 物料编码 - %s where 商品编号 = '%s'" % (count1, numb1)
            # print(sql)
            cur.execute(sql)
            db.commit()
            print('出库成功~~~出库后数量为：' + str(residue_count))
            db.close()
        else:
            print(numb1 + ' 型号库存不够啦~  当前库存为：'+ str(reality_numb) + ' 需要出库数量为：' + count1)

def excel_head(address):
    # 打开文件,默认打开第一个sheet
    workbook = xlrd.open_workbook(address)
    # sheet1,索引是从0开始,得到sheet1表的句柄.用这个可以操作表
    sheet1 = workbook.sheet_by_index(1)
    # 得到Excel的表头词条
    excel_head1 = sheet1.row_values(1)
    # 循环得到sheet1表的内容
    print(excel_head1)
    return excel_head1

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
    flag = 1   #   标记默认是格式化入库数据
    flag_index = 2   #   标记出库数量所在的Excel下标
# def read_excel_head(sheet1):
#     #得到Excel的表头词条
    excel_head = sheet1.row_values(1)
    # 循环得到sheet1表的内容
    print(excel_head)
    for j in range(len(excel_head)):
        if excel_head[j] == '出库数量':
            print('222')
            flag = 0  #   有出库数量则改为0  标记为格式化出库数据
            flag_index = j    #  标记下标

#     return excel_head
    print(flag_index)
# def formatting_list():
    #格式化数据
    if flag == 1 :
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
    else:
        print('出库')
        data_list = []
        numb_list = []
        for i in range(2, sheet1.nrows - 1):  # 循环行数
            # dict = []
            # print(sheet1.row_values(i)[flag_index])#获取行数据
            # dict.append(str(sheet1.row_values(i)[flag_index]))
            # print(dict)
            data_list.append(str(int(sheet1.row_values(i)[flag_index])))
            numb_list.append(sheet1.row_values(i)[1])
        print(data_list)
        print(numb_list)
        # change_db_out(numb_list, data_list)
    # print(len(data_list))
    # for i in range(len(data_list)):
    #     print(data_list[i][1] + "-" + data_list[i][9]+ "-" + str(i))
    #     change_db(inquire_db(data_list[i][1]), data_list[i][9])
    return data_list





if __name__ == '__main__':
    # sheet1 = get_excel(r'1.xls')
    # excel_head = read_excel_head(sheet1)
    data_list = get_excel(r'2.xls')
    eh = excel_head(r'2.xls')
    # db, cur = connect_db()
    # create_library()      #建库建表
    insert_db(data_list, eh)      #插入数据
    # number = 'C251614'
    # inquire_db(number)      #查数据（未完善）
    # quantity = 2      #需要增加的数量
    # serial_number = 'C235378'     #需要增加数量的型号
    # change_db(quantity, serial_number)      #修改数据库数据

    # cols = ", ".join('`{}`'.format(k) for k in eh)
    # print(cols)  # '`name`, `age`'
    # # cols = '`时间`, `来自`, `内容`'
    # # val_cols = ', '.join('%({})s'.format(k) for k in formatting_chars.keys())
    # val_cols = ', '.join('%({})s'.format(k) for k in eh)
    # print(val_cols)  # '%(name)s, %(age)s'
    # sql = "insert into test_an(%s) values(%s)"
    # res_sql = sql % (cols, val_cols)
    # print(res_sql)
