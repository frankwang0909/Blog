+++
url = "mysql-basic-2.html"
categories = ["Database"]
tags = ["MySQL"]
date = "2017-06-08T07:32:57+08:00"
title = "MySQL数据库的基本数据类型、表的操作和记录的操作"
description = "MySQL数据库的基本数据类型包括数值类型、字符类型和时间日期类型。MySQL数据库表的基本操作。MySQL数据库记录的基本操作"
+++

## 一、MySQL的基本数据类型：

### 1. 数值类型：
包括严格数值数据类型(INTEGER、SMALLINT、DECIMAL和NUMERIC)，以及近似数值数据类型(FLOAT、REAL和DOUBLE PRECISION)。

| 类型          | 大小    | 范围（有符号）    | 范围（无符号）    | 用途         |
| ------------- |:-------------:|:-----------:|:-----------------:| ------------:|
| TINYINT       | 1 字节  | (-128，127)       |(0，255)           |小整数值      |
| SMALLINT      | 2 字节  | (-2^15，2^15 -1)  |(0，2^16 -1)       |大整数值      |
| MEDIUMINT     | 3 字节  | (-2^23，2^23 -1)  |(0，2^24 -1)       |大整数值      |
| INT或INTEGER  | 4 字节  | (-2^31，2^31 -1)  |(0，2^32 -1)       |大整数值      |
| BIGINT        | 8 字节  |(-2^63，2^63 -1)   |(0，2^64 -1)       |极大整数值    |
| FLOAT         | 4 字节  |	(-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38)| 0，(1.175 494 351 E-38，3.402 823 466 E+38)|单精度浮点数值|
| DOUBLE        | 8 字节  |(-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)|0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)|双精度浮点数值|
| DECIMAL       | DECIMAL(M,D)。如果M>D，为M+2否则为D+2 |依附于M和D的值|依附于M和D的值|小数值  |


DECIMAL(M,D)：

M指定指定小数点左边和右边可以存储的十进制数字的最大个数，最大精度38。

D指定小数点右边可以存储的十进制数字的最大个数。小数位数必须是从 0 到 a之间的值。默认小数位数是 0。			


### 2. 字符型：

字符串类型主要包括CHAR、VARCHAR、TEXT、MEDIUMTEXT、LONGTEXT、EMU等。

| 类型      | 大小                     | 用途               |
| ----------|:------------------------:| ------------------:|
| CHAR      | 0~2^8-1 (0~255) 字节     | 定长字符串         |
| VARCHAR   | 0~2^16-1 (0~65536) 字节  | 变长字符串         |
| TINYTEXT  | 0~2^8-1 (0~255) 字节     | 短文本字符串       |
| TEXT      | 0~2^16-1 (0~65536)字节   | 长文本数据         |
|MEDIUMTEXT | 0~2^24-1 (0~16777215)字节| 中等长度文本数据   |
|LONGTEXT   | 0~2^32-1 (0~4294967296)  | 极大文本数据       |

定长字符串：没有达到指定长度，尾部空格补齐。

### 3. 日期时间类型：

表示时间值的日期和时间类型为DATETIME、DATE、TIMESTAMP、TIME和YEAR。

每个时间类型有一个有效值范围和一个"零"值，当指定不合法的MySQL不能表示的值时使用"零"值。

类型	大小
(字节)	范围	格式	用途
DATE	3	1000-01-01/9999-12-31	YYYY-MM-DD	日期值
TIME	3	'-838:59:59'/'838:59:59'	HH:MM:SS	时间值或持续时间
YEAR	1	1901/2155	YYYY	年份值
DATETIME	8	1000-01-01 00:00:00/9999-12-31 23:59:59	YYYY-MM-DD HH:MM:SS	混合日期和时间值
TIMESTAMP	4	1970-01-01 00:00:00/2037 年某时	YYYYMMDD HHMMSS	混合日期和时间值，时间戳

| 类型      | 大小    | 范围                                     | 格式               | 用途         |
| ----------|:-------:|:----------------------------------------:|:------------------:| ------------:|
| YEAR      | 1 字节  | 1901~2155                                |YYYY                |年份值        |
| DATE      | 3 字节  | 1000-01-01 ~ 9999-12-31                  |YYYY-MM-DD          |日期值        |
| TIME      | 3 字节  | -838:59:59 ~ 838:59:59                   |HH:MM:SS            |时间值或持续时间|
| DATETIME  | 8 字节  | 1000-01-01 00:00:00 ~ 9999-12-31 23:59:59  |YYYY-MM-DD HH:MM:SS |混合日期和时间值|
| TIMESTAMP | 4 字节  | 1970-01-01 00:00:00 ~ 2037                 |YYYYMMDD HHMMSS     |时间戳         |

## 二、数据表的操作：

### 1.查看当前数据库

	SELECT DATABASE();

### 2.创建数据表

	CREATE TABLE [IF NOT EXISTS] table_name ( column_name data_type,...);


	CREATE TABLE IF NOT EXISTS user(
		username VARCHAR(20),
		age TINYINT UNSIGNED,
		salary FLOAT(8,2) UNSIGNED
	);


### 3.查看数据表

	SHOW TABLES;

查看其它数据库的数据表

	SHOW TABLES FROM mysql;


### 4.查看数据表结构

	SHOW COLUMNS FROM tbl_name;

	SHOW COLUMNS FROM user;


## 三、记录的操作：

数据表里的行，被称为数据库的记录

### 1.插入记录

	INSERT [INFO] tbl_name [(col_name,..)] VALUES(val,..);
	
	INSERT user VALUES('Frank', 22, 3500.18);

如果省略了字段名（即列名），则值必须与字段的数量一致，否则会报错。

	Column count doesn't match value count at row 1

如果对某部分字段赋值，则需要写明字段名。
	
	INSERT user(username,salary)  VALUES('Jack', 4500.18);

### 2.查找记录

	SELECT expr,... FROM tbl_name;

查看全部记录

	SELECT * FROM tbl_name; 

	SELECT * FROM user;

### 3.空值

NULL, 字段值可以为空；
NOT NULL, 字段值不能为空。


CREATE TABLE tb2(
	username VARCHAR(20) NOT NULL,
	age TINYINT UNSIGNED NULL
);

### 4.自动编号：AUTO_INCREMENT

必须与主键组合使用。默认情况下，其实值为1，每次的增量为1.

	CREATE TABLE tb3(
		id SMALLINT UNSIGNED AUTO_INCREMENT,
		username VARCHAR(20) NOT NULL,
		age TINYINT UNSIGNED NULL
	);

报错：

	ERROR 1075(42000): Incorrect table definition; there can be only one auto column and it must be defined as a key.


### 5.主键：PRIMARY KEY

1）每张数据表只能存在一个主键；

2）主键保证记录的唯一性；

3）主键自动为NOT NULL.

创建数据表tb4:

	CREATE TABLE tb4(
		id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
		username VARCHAR(20) NOT NULL,
		age TINYINT UNSIGNED NULL
	);

插入记录：

	INSERT tb3(username) VALUES('Ross');
	INSERT tb3(username) VALUES('Richard');
	INSERT tb3(username) VALUES('Monica');


### 5.唯一约束：UNIQUE KEY

1）UNIQUE KEY可以保证记录的唯一性；

2）UNIQUE KEY可以为空值；

3）每张表里可以存在多个唯一约束。

创建数据表tb5:

	CREATE TABLE tb5(
		id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
		username VARCHAR(20) NOT NULL UNIQUE KEY,
		age TINYINT UNSIGNED NULL
	);

查看刚刚创建的数据表tb5数据结构：

	SHOW COLUMNS FROM tb5;

插入一条记录：

	INSERT tb5(username, age) VALUES('Ross', 30);

插入成功，现在已经有一条记录的`username`为'Ross'了。再插入一条记录：

	INSERT tb5(username, age) VALUES('Ross', 28);

报错：

	ERROR 1062 (23000): Duplicate entry 'Ross' for key 'username'

### 6.默认值： DEFAULT
当插入记录时，如果没有明确为字段赋值，则自动赋予默认值。

	CREATE TABLE tb6(
		id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
		username VARCHAR(20) NOT NULL UNIQUE KEY,
		sex ENUM('1', '2', '3') DEFAULT '3'
	);

查看刚刚创建的数据表tb6数据结构：

	SHOW COLUMNS FROM tb6;

插入一条记录：
	
	INSERT tb6(username) VALUES('Frank');

查看记录：
	
	SELECT * FROM tb6;



