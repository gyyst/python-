import sqlite3






conn=sqlite3.connect("test.db")#打开或创建数据库文件
#
#
# print("成功打开数据库")
# c=conn.cursor()#获得游标
# sql='''
#     create table company
#     (id int primary key not null,
#     name text not null,
#     age int not null,
#     address char(50),
#     salary real);
#
#
# '''
# c.execute(sql)#执行sql语句
# conn.commit()#提交数据库操作
#
# print("成功建表")
#3.插入数据
c=conn.cursor()
sql1='''
    insert into company (id,name,age,address,salary)
    values(1,'张三',32,'chengdu',8000);
'''

sql2='''
    insert into company (id,name,age,address,salary)
    values(2,'李四',38,'chongqing',8800);
'''

c.execute(sql1)
c.execute(sql2)

conn.commit()
print("成功插入数据")
#4.查询数据

sql3="select id,name,address,salary from company"
cursor=c.execute(sql3)
for row in cursor:
    print("id=",row[0])
    print("name=",row[1])
    print("address=",row[2])
    print("salary=",row[3],"\n")

print("查询完毕")

conn.close()