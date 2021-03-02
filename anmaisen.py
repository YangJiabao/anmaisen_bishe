import xlrd
import pymysql

def get_excel(address):
    # 打开文件
    workbook = xlrd.open_workbook(address)
    # sheet1,索引是从0开始,得到sheet1表的句柄.用这个可以操作表
    sheet1 = workbook.sheet_by_index(1)
    # 表名
    print(sheet1.name)
    # 有效行数
    print(sheet1.nrows)
    # 有效列数
    print(sheet1.ncols)
    return sheet1

def read_excel_head(sheet1):
    excel_head = sheet1.row_values(1)
    # 循环得到sheet1表的内容
    print(excel_head)
    return excel_head

def formatting_list(sheet1):
    # 打开文件
    excel_list = {}
    # workbook = xlrd.open_workbook(r'1.xls')
    # # 获取所有的sheet的名字
    # print(workbook.sheet_names())
    # # 获取第二个sheet的表名
    # sheets_name = workbook.sheets()
    # print(sheets_name)
    # 循环得到sheet1表的内容
    for i in range(sheet1.ncols):
        # print(sheet1.col_values(i)[1])
        text = []
        # tup = ()
        excel_list[sheet1.col_values(i)[1]] = sheet1.col_values(i)[2:-1]
        # excel_list.append(text)
        # text[sheet1.col_values(i)[1]] = sheet1.col_values(i)[2:-1]
        # print(sheet1.col_values(i)[2:-1])
        # excel_list.append(text)
    print(excel_list)
    print(111)
    return excel_list

def read_excel_list(sheet1):
    # 打开文件
    excel_list = []
    text = {}
    tup = ()
    for i in range(sheet1.ncols):
        # # print(sheet1.col_values(i)[1])

        text[sheet1.col_values(i)[1]] = sheet1.col_values(i)[2:-1]
        # print(sheet1.col_values(i)[2:-1])
        # excel_list.append(tuple(sheet1.col_values(i)[1:-1]))
    tup = tup[:] + (text,)
    print(tup)
    print(text)
    print(222)
    excel_list.append(tup)
    print(excel_list)
    return text

sheet1 = get_excel(r'1.xls')
excel_head = read_excel_head(sheet1)
formatting_chars =  formatting_list(sheet1)
excel_list = []
excel_list.append(formatting_chars)
print(excel_list)
excel_list1 = read_excel_list(sheet1)
# print(excel_list1)
# print(excel_list)

cols = ", ".join('`{}`'.format(k) for k in formatting_chars.keys())
print(cols)  # '`name`, `age`'
# cols = '`时间`, `来自`, `内容`'
# val_cols = ', '.join('%({})s'.format(k) for k in formatting_chars.keys())
val_cols = ', '.join('%({})s'.format(k) for k in formatting_chars.keys())
print(val_cols)  # '%(name)s, %(age)s'



# #打开数据库，数据库可自己创建，create database test;
# con = pymysql.connect(host='localhost', user='root', passwd='19971012', db='anmaisen', port=3306, charset='utf8')
# #通过cursor()创建一个游标对象
# cur = con.cursor()


# 建库和建表
db = pymysql.connect(host='localhost', user='root',
                      passwd='19971012', db='text',charset='utf8')
cur = db.cursor()


sql = "insert into test_an1(%s) values(%s)"
res_sql = sql % (cols, val_cols)
print(res_sql)  # 'insert into users(`name`, `age`) values(%(name)s, %(age)s)'
cur.execute(res_sql, formatting_chars)#批量化插入  列表   列表里必须是元组
# cursor.executemany('insert into weibo values( %s,  %s, %s)'

db.commit()# 提交到数据库执行
# 关闭数据库连接
db.close()



# # 开始建库
# cur.execute("create database text character set utf8;")
# a = ["你好", "我好", "大家好"]
# 建表
# sql = """
#       create table test_an1(
#           `%s` varchar(255),
#           `%s` varchar(255),
#           `%s` varchar(255),
#           `%s` varchar(255),
#           `%s` varchar(255),
#           `%s` varchar(255),
#           `%s` varchar(255),
#           `%s` varchar(255),
#           `%s` varchar(255),
#           `%s` varchar(255),
#           `%s` varchar(255),
#           `%s` varchar(255))
#       """
# cur.execute(sql,excel_head)
# db.close()

# sql = """INSERT INTO test_an1(购买类型,
#         商品编号, 物料编码)
#          VALUES (%s, %s, %s)"""
#
# try:
#     # 执行sql语句
#     cur.execute(sql,a)
#     print(111)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 如果发生错误则回滚
#     db.rollback()
#     print('err')



# sql插入语句 表名blogs
# cur_insert = db.cursor()
# a = ['2','232','34']
# sql_insert ="""insert into test_an1(你好,我好,大家好) values (%s,%s,%s)"""
#
# try:
#     cur_insert.execute(sql_insert, a)
#     # 提交
#     db.commit()
#     print('开始数据库插入操作')
# except Exception as e:
#     db.rollback()
#     print('数据库插入操作错误回滚')
# finally:
#     db.close()
