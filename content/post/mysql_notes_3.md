+++

categories = ["Database"]
tags = ["MySQL"]
date = "2017-06-27T22:57:29+08:00"
title = "MySQL学习笔记：修改数据表的常用命令"
keywords = ["MySQL学习笔记", "修改数据表"]
description = "MySQL学习笔记：修改数据表的常用命令，包括新增或删除数据列的命令，新增约束，删除约束，修改数据列的定义，修改数据列的名称，数据表更名"
url = "/mysql_notes_3.html"

+++

## 1.新增或删除列

1.1 添加单列

语法：`ALTER TABLE tbl_name ADD [COLUMN] col_name col_definition [FIRST | AFTER col_name];`

指定位置关系的关键字：

1.FIRST：表示在数据表的第一列

2.AFTER: 参数col_name为某个数据列的名称，表示指定在该数据列的后面。

示例代码如下：

	ALTER TABLE users ADD age TINYINT UNSIGNED NOT NULL DEFAULT 10;

	ALTER TABLE users ADD password VARCHAR(20) NOT NULL AFTER username;

	ALTER TABLE users ADD truename VARCHAR(20) NOT NULL FIRST;


1.2 添加多列（不能指定位置关系）

	ALTER TABLE tbl_name ADD [COLUMN] (col_name1 col_definition, col_name2 col_definition,...);


1.3 删除列

语法：`ALTER TABLE tbl_name DROP col_name1 [, DROP col_name2];

	ALTER TABLE users DROP truename;


## 2.添加约束

2.1 添加主键约束：(数据表只能有一个主键)

语法：`ALTER TABLE tbl_name ADD [CONSTRAINT [symbol]] PRIMARY KEY [index_type] (index_col_name);`

	ALTER TABLE users3 ADD CONSTRAINT PK_users2_id PRIMARY KEY (id);


2.2 添加唯一约束：唯一约束可以有多个

语法：` ALTER TABLE tbl_name ADD [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY] [index_name] [ index_type] (index_col_name, ...);`

	ALTER TABLE users3 ADD UNIQUE (username);

2.3 添加外键约束：

语法：` ALTER TABLE tbl_name ADD [CONSTRAINT [symbol]] FOREIGN KEY [index_name] (index_colo_name) reference_definition;`

	ALTER TABLE users3 ADD FOREIGEN KEY (pid) REFERENCE provinces (id);

2.4 添加默认约束：

语法：`ALTER TABLE tbl_name ALTER [COLUMN] col_name SET DEFAULT literal;`

给 age 字段添加默认约束，默认值为10：

	ALTER TABLE users3 ALTER age SET DEFAULT 10;


## 3.删除约束：

3.1 删除主键约束：

	ALTER TABLE users DROP PRIMARY KEY;

3.2 删除唯一约束：

	ALTER TABLE users DROP INDEX username;

3.3 删除外键约束：需指定外键名称

	ALTER TABLE tbl_name DROP FOREIGN KEY fk_symbol

fk_symbol 是系统赋予外键的名字，通过如下命令可以查看到 

	SHOW CREATE TABLE users;

	ALTER TABLE users DROP FOREIGN KEY users_ibfk_1;

3.4 删除默认约束：需指定字段

	ALTER TABLE tbl_name ALTER [COLUMN] col_name DROP DEFAULT

比如：删除age 字段的默认约束

	ALTER TABLE users3 ALTER age DROP DEFAULT;

## 4.修改列定义：

	ALTER TABLE tbl_name MODIFY [COLUMN] col_name col_definition [FIRST | AFTER col_name]

	ALTER TABLE users MODIFY pid SMALLINT UNSIGNED NOT NULL FIRST;


## 5.修改列的名称：

	ALTER TABLE tbl_name CHANGE [COLUMN] old_col_name new_col_name column_definition [FIRST | AFTER col_name]


## 6.数据表更名：

	ALTER TABLE tbl_name RENAME [TO|AS] new_tbl_name;

或者

	RENAME TABLE tbl_name TO new_tbl_name [, tbl_name2 TO new_tbl_name2 ,...]

方法2可以同时为多张数据表更名。
