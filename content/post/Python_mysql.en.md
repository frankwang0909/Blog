+++
title = "Python Mysql"
keywords = ["Python", "MySQL", "MySQLdb", "Database connection object connection", "Database interaction object cursor", "study notes"]
description = "Python operates MySQL and accesses the unified standardized interface of the database Python DB API"
categories = ["Python", "Database"]
tags = ["Python", "MySQL"]
date = "2017-06-20T07:44:01+08:00"
url = "/python_mysqldb.html"
+++


## 1. Application architecture

Client --> Business logic layer --> Data access layer --> Database


## 2. Python DB API

Python application (including SQL) --> Python DB API (unified and standardized interface for accessing database MySQLdb) --> MySQL/Oracle/SQLServer and other databases

1. Database connection object: connection

2. Database interaction object: cursor

3. Database exception class: exceptions



## 3. Access database process:

Create connection object connection --> Get interactive object cursor --> Execute query/execute command/get data/process data, etc. --> Close cursor --> Close connection


## 4. Database connection object: connection

1. Establish a network connection between the Python client and the database

2. Creation method: MySQLdb.Connect()

3. Parameters:


host database server address

port port number, numeric type

user username

passwd password

db database name

charset encoding format, utf8



4. Method:

cursor() gets the interactive object (cursor)

commit() commits the current transaction

rollback() rolls back the current transaction

close() closes the connection

## 5. Database interaction object (cursor) cursor: used to execute queries and obtain results

1. Method:

1) execute(op [, args] ) executes SQL and obtains the results from the database to the client. There is a local buffer.


2) fetch*() method: move the pointer rownumber and return data.

fetchone() gets the next row of the result set

fetchmany(size) gets the next few rows of the result set

fetchall() gets all the remaining rows in the result set


3) close() closes the cursor object


2. Attribute: rowcount The number of rows of data returned by the latest execution or the number of affected rows.



## 6. Affairs

1. A program execution unit that accesses and updates the database, which can contain multiple SQL statements or command operations.

2. The engine must be set to INNODB.

3. Features:

1) Atomicity: All operations included in the transaction are either not performed or are performed.

2) Consistency: A transaction must change the database from a consistent state to another consistent state.

3) Isolation: The execution of a transaction cannot be interfered with by other transactions.

4) Durability: Once a transaction is committed, its changes to the database are permanent.


4. Use transactions:

1) Turn off automatic commit: set conn.autocommit(False);

2) End the transaction normally: conn.commit();

3) Abnormal end of transaction: conn.rollback().



