+++

categories = ["Database"]
tags = ["MySQL"]
date = "2017-06-27T22:57:29+08:00"
title = "Mysql Notes 3"
keywords = ["MySQL study notes", "Modify data table"]
description = "MySQL study notes: Common commands for modifying data tables, including commands to add or delete data columns, add constraints, delete constraints, modify the definition of data columns, modify the names of data columns, and rename the data table"
url = "/mysql_notes_3.html"

+++

## 1. Add or delete columns

1. 1 Add a single column

Syntax: `ALTER TABLE tbl_name ADD [COLUMN] col_name col_definition [FIRST | AFTER col_name];`

Keywords that specify positional relationships:

1. FIRST: Indicated in the first column of the data table

2. AFTER: The parameter col_name is the name of a data column, which means it is specified after the data column.

The sample code is as follows:

ALTER TABLE users ADD age TINYINT UNSIGNED NOT NULL DEFAULT 10;

ALTER TABLE users ADD password VARCHAR(20) NOT NULL AFTER username;

ALTER TABLE users ADD truename VARCHAR(20) NOT NULL FIRST;


1. 2 Add multiple columns (positional relationship cannot be specified)

ALTER TABLE tbl_name ADD [COLUMN] (col_name1 col_definition, col_name2 col_definition,...);


1. 3 Delete columns

Syntax: `ALTER TABLE tbl_name DROP col_name1 [, DROP col_name2];

ALTER TABLE users DROP truename;


## 2. Add constraints

2. 1 Add primary key constraints: (data table can only have one primary key)

Syntax: `ALTER TABLE tbl_name ADD [CONSTRAINT [symbol]] PRIMARY KEY [index_type] (index_col_name);`

ALTER TABLE users3 ADD CONSTRAINT PK_users2_id PRIMARY KEY (id);


2. 2 Add unique constraints: There can be multiple unique constraints

Syntax: ` ALTER TABLE tbl_name ADD [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY] [index_name] [ index_type] (index_col_name, ...);`

ALTER TABLE users3 ADD UNIQUE (username);

2. 3 Add foreign key constraints:

Syntax: `ALTER TABLE tbl_name ADD [CONSTRAINT [symbol]] FOREIGN KEY [index_name] (index_colo_name) reference_definition;`

ALTER TABLE users3 ADD FOREIGEN KEY (pid) REFERENCE provinces (id);

2. 4 Add default constraints:

Syntax: `ALTER TABLE tbl_name ALTER [COLUMN] col_name SET DEFAULT literal;`

Add a default constraint to the age field, with a default value of 10:

ALTER TABLE users3 ALTER age SET DEFAULT 10;


## 3. Delete constraints:

3. 1 Delete primary key constraints:

ALTER TABLE users DROP PRIMARY KEY;

3. 2 Delete the unique constraint:

ALTER TABLE users DROP INDEX username;

3. 3 Delete foreign key constraints: you need to specify the foreign key name

ALTER TABLE tbl_name DROP FOREIGN KEY fk_symbol

fk_symbol is the name assigned to the foreign key by the system, which can be viewed through the following command

SHOW CREATE TABLE users;

ALTER TABLE users DROP FOREIGN KEY users_ibfk_1;

3. 4 Delete default constraints: fields need to be specified

ALTER TABLE tbl_name ALTER [COLUMN] col_name DROP DEFAULT

For example: delete the default constraint on the age field

ALTER TABLE users3 ALTER age DROP DEFAULT;

## 4. Modify column definition:

ALTER TABLE tbl_name MODIFY [COLUMN] col_name col_definition [FIRST | AFTER col_name]

ALTER TABLE users MODIFY pid SMALLINT UNSIGNED NOT NULL FIRST;


## 5. Modify the name of the column:

ALTER TABLE tbl_name CHANGE [COLUMN] old_col_name new_col_name column_definition [FIRST | AFTER col_name]


## 6. Data table rename:

ALTER TABLE tbl_name RENAME [TO|AS] new_tbl_name;

or

RENAME TABLE tbl_name TO new_tbl_name [, tbl_name2 TO new_tbl_name2 ,...]

Method 2 can rename multiple data tables at the same time.
