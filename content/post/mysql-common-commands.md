+++
date = "2017-06-03T22:38:52+08:00"
title = "MySQL入门：语句规范及常用命令"
keywords = ["MySQL", "语句规范", "常用命令"]
description = "MySQL入门：MySQL语句规范及MySQL的常用命令。MySQL语句规范：关键字、函数名全部大写；数据库名、表名、字段名一律小写；SQL语句必须以分号结尾。MySQL的常用命令：创建数据库， 查看数据库，删除数据库等。"
menu = "Database"
categories = ["Database"]
tags = ["MySQL"]
url = "/mysql-basic.html"
+++


## 一、MySQL语句规范：

1.关键字、函数名全部大写；

2.数据库名、表名、字段名一律小写；

3.SQL语句必须以分号结尾。

## 二、MySQL常用命令：

1.显示当前数据库版本

	SELECT VERSION();

2.显示当前时间:

	SELECT NOW();

3.显示当前用户：

	SELECT USER();

4.创建数据库：

语法为：

	CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name [DEFAULT] CHARACTER SET [=] charset_name;

输入如下语句，将会创建数据库test2:
	
	CREATE DATABASE test2;


如果数据库test2已经存在，将会报错：

	ERROR 1007 (HY000): Can't create database 'test2'; database exists

如果创建数据库的时候加了 `IF NOT EXISTS`, 遇到已经存在的数据库，将不会报错，但会有一条`WARNING`.

	CREATE DATABASE IF NOT EXISTS test2;
	Query OK, 1 row affected, 1 warning (0.00 sec)

如果想要查看WARNING信息，只需输入`SHOW WARNING;`.

4.查看数据库：

语法为：

	SHOW {DATABASES | SCHEMAS} [LIKE 'pattern' | WHERE expr];

输入如下语句，可以查看

	SHOW DATABASES;

5.删除数据库：

语法：

	DROP {DATABASE | SCHEMA} [IF EXISTS] db_name

如果数据库test2, 输入以下语句，可以删除该数据库：

	DROP DATABASE test2;

如果需要删除的数据库test2不存在，则会报错。
	
	ERROR 1008 (HY000): Can't drop database 'test2'; database doesn't exist

如果删除时添加了 `IF EXISTS`，则不会报错，而是会有一条WARNING:
	
	DROP DATABASE IF EXISTS test2;
	Query OK, 1 row affected, 1 warning (0.00 sec)