+++
title = "Win7系统MySQL报错ERROR1045及其处理方法"
menu = "Database"
description = "Win7系统安装MySQL报错ERROR1045及其处理方法"
categories = ["Database"]
tags = ["MySQL"]
date = "2017-06-03T21:52:09+08:00"
url = "mysql-error-1045.html"
+++

最近自学数据库，在`Win7`系统下使用`MySQL`遇到了一些报错，做个记录，方便以后查阅。

MySQL官网下载的`MySQL 5.5.56`的社区版，安装正常。当我在命令行输入`mysql -u root -p` 出现了报错信息，无法连接数据库。

	C:\Windows\system32> mysql -u root -p
	Enter password: 
	ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
 

网上找到的解决方法如下：

1.编辑mysql配置文件`my.ini`，在`[mysqld]`这个条目下加入
  
	skip-grant-tables


2.保存`my.ini`退出后重启mysql。

命令行输入 `net stop mysql` 停止MySQL服务；

命令行输入 `net start mysql` 重启MySQL服务；

3.重置密码：
现在在命令行输入`mysql -u root -p`就可以不用密码登录了，出现`password：`的时候直接回车可以进入，不会出现`ERROR 1045 (28000)`。

1）进入mysql数据库：输入`use mysql`, 会出现`Database changed`的提示信息。

	mysql> use mysql;

	Database changed

2）给root用户设置新密码：输入`update user set password=password("新密码") where user="root";`

	mysql> update user set password=password("新密码") where user="root";
	Query OK, 1 rows affected (0.01 sec)
	Rows matched: 1 Changed: 1 Warnings: 0

3)刷新数据库: 输入`flush privileges;`

	mysql> flush privileges;
	Query OK, 0 rows affected (0.00 sec)

4)退出mysql：输入`quit`

	mysql> quit
	Bye

4.重新修改配置文件`my.ini`，把刚才加入的`skip-grant-tables`这行代码删除，保存退出再重启mysql服务就可以了。
