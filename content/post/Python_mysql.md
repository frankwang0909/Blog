+++
title = "Python操作MySQL学习笔记"
keywords = "Python, MySQL, MySQLdb, 数据库连接对象connection, 数据库交互对象cursor, 学习笔记"
description = "Python操作MySQL，访问数据库的统一规范接口Python DB API"
categories = ["Python", "Database"]
tags = ["Python", "MySQL"]
date = "2017-06-20T07:44:01+08:00"
url = "/python_mysqldb.html"
+++


## 一、应用架构

客户端 --> 业务逻辑层 --> 数据访问层 --> 数据库


## 二、 Python DB API

Python应用程序（包含SQL) --> Python DB API（访问数据库的统一规范接口MySQLdb） --> MySQL / Oracle / SQLServer等数据库

1.数据库连接对象：connection

2.数据库交互对象：cursor

3.数据库异常类: exceptions



## 三、访问数据库流程：

创建连接对象connection --> 获取交互对象cursor --> 执行查询/执行命令/获取数据/处理数据等 --> 关闭cursor --> 关闭connection


## 四、数据库连接对象：connection

1. 建立Python客户端与数据库的网络连接

2. 创建方法： MySQLdb.Connect()

3. 参数：


	host 数据库服务器地址

	port 端口号， 数字类型

	user 用户名

	passwd 密码

	db 数据库名称

	charset 编码格式, utf8



4.方法：

cursor() 获取交互对象（游标）

commit() 提交当前事务

rollback() 回滚当前事务

close() 关闭连接

## 五、数据库交互对象（游标）cursor: 用于执行查询和获取结果

1.方法：

1）execute(op [, args] )    执行SQL,将结果从数据库获取到客户端，存在本地缓冲区。


2）fetch*() 方法：移动指针rownumber， 返回数据。

fetchone() 获取结果集的下一行

fetchmany(size) 获取结果集的下几行

fetchall() 获取结果集中剩下的所有行


3）close() 关闭游标对象


2.属性：rowcount 最近一次execute返回数据的行数或影响的行数。



## 六、事务

1.访问和更新数据库的一个程序执行单元，可以包含多个SQL语句或命令的操作。

2.必须设置引擎为INNODB。

3.特性：

1）原子性：事务包含的所有操作，要么不做，要么都做。

2）一致性：事务必须使数据库从一致性状态变到另一个一致性状态。

3）隔离性：一个事务的执行不能被其他事务所干扰。

4）持久性：事务一旦提交，它对数据库的改变就是永久性的。


4.使用事务：

1）关闭自动commit：设置conn.autocommit(False);

2）正常结束事务：conn.commit();

3）异常结束事务：conn.rollback().





