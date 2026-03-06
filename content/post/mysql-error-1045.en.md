+++
title = "Mysql Error 1045"
keywords = ["MySQL error"]
description = "Win7 system installation MySQL error ERROR1045 and how to deal with it"
categories = ["Database"]
tags = ["MySQL"]
date = "2017-06-03T21:52:09+08:00"
url = "/mysql-error-1045.html"
+++

I recently learned databases by myself and encountered some errors when using `MySQL` under the `Win7` system. I made a record for future reference.

The community version of `MySQL 5.5.56` was downloaded from the MySQL official website and installed normally. When I enter `mysql -u root -p` on the command line, an error message appears and I cannot connect to the database.

C:\Windows\system32> mysql -u root -p
	Enter password:
	ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
 

The solutions found online are as follows:

1. Edit the mysql configuration file `my.ini` and add it under the entry `[mysqld]`
  
skip-grant-tables


2. Save `my.ini` and exit and then restart mysql.

Enter `net stop mysql` on the command line to stop the MySQL service;

Enter `net start mysql` on the command line to restart the MySQL service;

3. Reset password:
Now enter `mysql -u root -p` on the command line to log in without a password. When `password:` appears, just press Enter to enter. `ERROR 1045 (28000)` will not appear.

1) Enter the mysql database: enter `use mysql`, and the prompt message `Database changed` will appear.

mysql> use mysql;

Database changed

2) Set a new password for the root user: enter `update user set password=password("new password") where user="root";`

mysql> update user set password=password("new password") where user="root";
	Query OK, 1 rows affected (0.01 sec)
	Rows matched: 1 Changed: 1 Warnings: 0

3) Refresh the database: Enter `flush privileges;`

mysql> flush privileges;
	Query OK, 0 rows affected (0.00 sec)

4) Exit mysql: enter `quit`

mysql> quit
	Bye

4. Re-modify the configuration file `my.ini`, delete the line of code `skip-grant-tables` that was just added, save and exit, and then restart the mysql service.
