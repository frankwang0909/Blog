+++
url = "/mysql-basic-2.html"
categories = ["Database"]
tags = ["MySQL"]
date = "2017-06-08T07:32:57+08:00"
title = "Mysql Basic 2"
description = "The basic data types of MySQL database include numeric types, character types and time and date types. Basic operations on MySQL database tables. Basic operations of MySQL database records"
+++

## 1. Basic data types of MySQL:

### 1. Numeric type:
Includes strict numeric data types (INTEGER, SMALLINT, DECIMAL, and NUMERIC), as well as approximate numeric data types (FLOAT, REAL, and DOUBLE PRECISION).

| type | size | range (signed) | range (unsigned) | purpose |
| ------------- |:-------------:|:----------:|:------------------:| ------------:|
| TINYINT | 1 byte | (-128, 127) | (0, 255) | small integer value |
| SMALLINT | 2 bytes | (-2^15, 2^15 -1) | (0, 2^16 -1) | Large integer value |
| MEDIUMINT | 3 bytes | (-2^23, 2^23 -1) | (0, 2^24 -1) | Large integer value |
| INT or INTEGER | 4 bytes | (-2^31, 2^31 -1) | (0, 2^32 -1) | Large integer value |
| BIGINT | 8 bytes | (-2^63, 2^63 -1) | (0, 2^64 -1) | Very large integer value |
| FLOAT | 4 bytes | (-3.402 823 466 E+38, -1.175 494 351 E-38), 0, (1.175 494 351 E-38, 3.402 823 466 351 E+38) | 0, (1.175 494 351 E-38, 3.402 823 466 E+38)|Single precision floating point value|
| DOUBLE | 8 bytes | (-1.797 693 134 862 315 7 E+308, -2.225 073 858 507 201 4 E-308), 0, (2.225 073 858 507 201 4 E-308, 1.797 693 134 862 315 7 E+308)|0, (2.225 073 858 507 201 4 E-308, 1.797 693 134 862 315 7 E+308)|Double precision floating point value|
| DECIMAL | DECIMAL(M,D). If M>D, M+2 otherwise D+2 | Values ​​attached to M and D | Values ​​attached to M and D | Decimal value |


DECIMAL(M,D)：

M specifies the maximum number of decimal digits that can be stored to the left and right of the specified decimal point, with a maximum precision of 38.

D specifies the maximum number of decimal digits that can be stored to the right of the decimal point. The number of decimal places must be a value from 0 to a. The default number of decimal places is 0.


### 2. Character type:

String types mainly include CHAR, VARCHAR, TEXT, MEDIUMTEXT, LONGTEXT, EMU, etc.

| Type | Size | Purpose |
| ----------|:------------------------:| ------------------:|
| CHAR | 0~2^8-1 (0~255) bytes | fixed-length string |
| VARCHAR | 0~2^16-1 (0~65536) bytes | Variable length string |
| TINYTEXT | 0~2^8-1 (0~255) bytes | short text string |
| TEXT | 0~2^16-1 (0~65536) bytes | Long text data |
|MEDIUMTEXT | 0~2^24-1 (0~16777215) bytes | Medium length text data |
|LONGTEXT | 0~2^32-1 (0~4294967296) | Very large text data |

Fixed-length string: If it does not reach the specified length, trailing spaces will be padded.

### 3. Date and time type:

The date and time types that represent time values ​​are DATETIME, DATE, TIMESTAMP, TIME, and YEAR.

Each time type has a range of valid values ​​and a "zero" value, which is used when specifying an illegal value that MySQL cannot represent.

Type Size
(Bytes) Range Format Purpose
DATE 3 1000-01-01/9999-12-31 YYYY-MM-DD date value
TIME 3 '-838:59:59'/'838:59:59' HH:MM:SS time value or duration
YEAR 1 1901/2155 YYYY year value
DATETIME 8 1000-01-01 00:00:00/9999-12-31 23:59:59 YYYY-MM-DD HH:MM:SS Mixed date and time values
TIMESTAMP 4 1970-01-01 00:00:00/Sometime in 2037 YYYYMMDD HHMMSS Mixed date and time value, timestamp

| type | size | range | format | purpose |
| ----------|:-------:|:------------------------------------------------:|:------------------:| ------------:|
| YEAR | 1 byte | 1901~2155 |YYYY |Year value |
| DATE | 3 bytes | 1000-01-01 ~ 9999-12-31 |YYYY-MM-DD |Date value |
| TIME | 3 bytes | -838:59:59 ~ 838:59:59 |HH:MM:SS |Time value or duration|
| DATETIME | 8 bytes | 1000-01-01 00:00:00 ~ 9999-12-31 23:59:59 |YYYY-MM-DD HH:MM:SS |Mixed date and time values |
| TIMESTAMP | 4 bytes | 1970-01-01 00:00:00 ~ 2037 |YYYYMMDD HHMMSS |Timestamp |

## 2. Data table operations:

### 1. View the current database

SELECT DATABASE();

### 2. Create data table

CREATE TABLE [IF NOT EXISTS] table_name ( column_name data_type,...);


CREATE TABLE IF NOT EXISTS user(
		username VARCHAR(20),
		age TINYINT UNSIGNED,
		salary FLOAT(8,2) UNSIGNED
	);


### 3. View data table

SHOW TABLES;

View data tables from other databases

SHOW TABLES FROM mysql;


### 4. View the data table structure

SHOW COLUMNS FROM tbl_name;

SHOW COLUMNS FROM user;


## 3. Recording operations:

The rows in the data table are called database records

### 1. Insert records

INSERT [INFO] tbl_name [(col_name,..)] VALUES(val,..);
	
INSERT user VALUES('Frank', 22, 3500.18);

If the field name (i.e. column name) is omitted, the value must be consistent with the number of fields, otherwise an error will be reported.

Column count doesn't match value count at row 1

If you assign a value to some fields, you need to specify the field name.
	
INSERT user(username,salary) VALUES('Jack', 4500.18);

### 2. Find records

SELECT expr,... FROM tbl_name;

View all records

SELECT * FROM tbl_name;

SELECT * FROM user;

### 3. Null value

NULL, the field value can be empty;
NOT NULL, field value cannot be empty.


CREATE TABLE tb2(
	username VARCHAR(20) NOT NULL,
	age TINYINT UNSIGNED NULL
);

### 4. Automatic numbering: AUTO_INCREMENT

Must be used in combination with primary key. By default, the actual value is 1, and the increment is 1 each time.

CREATE TABLE tb3(
		id SMALLINT UNSIGNED AUTO_INCREMENT,
		username VARCHAR(20) NOT NULL,
		age TINYINT UNSIGNED NULL
	);

Error reported:

ERROR 1075(42000): Incorrect table definition; there can be only one auto column and it must be defined as a key.


### 5. Primary key: PRIMARY KEY

1) Each data table can only have one primary key;

2) The primary key ensures the uniqueness of the record;

3) The primary key is automatically NOT NULL.

Create data table tb4:

CREATE TABLE tb4(
		id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
		username VARCHAR(20) NOT NULL,
		age TINYINT UNSIGNED NULL
	);

Insert record:

INSERT tb3(username) VALUES('Ross');
	INSERT tb3(username) VALUES('Richard');
	INSERT tb3(username) VALUES('Monica');


### 5.Unique constraint: UNIQUE KEY

1) UNIQUE KEY can ensure the uniqueness of records;

2) UNIQUE KEY can be null;

3) Multiple unique constraints can exist in each table.

Create data table tb5:

CREATE TABLE tb5(
		id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
		username VARCHAR(20) NOT NULL UNIQUE KEY,
		age TINYINT UNSIGNED NULL
	);

View the tb5 data structure of the data table just created:

SHOW COLUMNS FROM tb5;

Insert a record:

INSERT tb5(username, age) VALUES('Ross', 30);

The insertion is successful, and there is now a record with `username` as 'Ross'. Insert another record:

INSERT tb5(username, age) VALUES('Ross', 28);

Error reported:

ERROR 1062 (23000): Duplicate entry 'Ross' for key 'username'

### 6.Default value: DEFAULT
When a record is inserted, if a field is not explicitly assigned a value, a default value is automatically assigned.

CREATE TABLE tb6(
		id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
		username VARCHAR(20) NOT NULL UNIQUE KEY,
		sex ENUM('1', '2', '3') DEFAULT '3'
	);

View the data structure of the data table tb6 just created:

SHOW COLUMNS FROM tb6;

Insert a record:
	
INSERT tb6(username) VALUES('Frank');

View records:
	
SELECT * FROM tb6;

