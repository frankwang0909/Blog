+++
date = "2017-06-03T22:38:52+08:00"
title = "Mysql Common Commands"
keywords = ["MySQL", "Statement specification", "Common commands"]
description = "Getting started with MySQL: MySQL statement specifications and common MySQL commands. MySQL statement specifications: keywords and function names are all in uppercase; database names, table names, and field names are all in lowercase; SQL statements must end with a semicolon. Common commands for MySQL: create database, view database, delete database, etc."
menu = "Database"
categories = ["Database"]
tags = ["MySQL"]
url = "/mysql-basic.html"
+++


## 1. MySQL statement specifications:

1. Keywords and function names should be in all capital letters;

2. Database names, table names, and field names must all be lowercase;

3. SQL statements must end with a semicolon.

## 2. Common MySQL commands:

1. Display the current database version

SELECT VERSION();

2. Display the current time:

SELECT NOW();

3. Display the current user:

SELECT USER();

4. Create a database:

The syntax is:

CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name [DEFAULT] CHARACTER SET [=] charset_name;

Enter the following statement to create database test2:
	
CREATE DATABASE test2;


If database test2 already exists, an error will be reported:

ERROR 1007 (HY000): Can't create database 'test2'; database exists

If you add `IF NOT EXISTS` when creating the database, no error will be reported when encountering an existing database, but there will be a `WARNING`.

CREATE DATABASE IF NOT EXISTS test2;
	Query OK, 1 row affected, 1 warning (0.00 sec)

If you want to see WARNING information, just enter `SHOW WARNING;`.

4. View the database:

The syntax is:

SHOW {DATABASES | SCHEMAS} [LIKE 'pattern' | WHERE expr];

Enter the following statement to view

SHOW DATABASES;

5. Delete the database:

grammar:

DROP {DATABASE | SCHEMA} [IF EXISTS] db_name

If database test2 is entered, enter the following statement to delete the database:

DROP DATABASE test2;

If the database test2 that needs to be deleted does not exist, an error will be reported.
	
ERROR 1008 (HY000): Can't drop database 'test2'; database doesn't exist

If `IF EXISTS` is added when deleting, no error will be reported, but a WARNING:
	
DROP DATABASE IF EXISTS test2;
	Query OK, 1 row affected, 1 warning (0.00 sec)