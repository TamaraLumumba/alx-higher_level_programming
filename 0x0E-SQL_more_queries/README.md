<div align="center">
  <h1> SQL - MORE QUERIES </h1>
  
</div>

## 0x00.Table of contents

* [Introduction](#-Introduction)
* [Learning-Objectives](#-Learning-Objectives)
* [Comments](#-Comments)
* [Requirments](#-Requirments)

## Introduction

In this project, I will be tackling the fundamentals of databases, where we will explore their core principles. Databases serve as structured digital repositories for efficiently storing and managing data. We'll delve into the different types of databases, such as relational databases, document-based databases, and key-value stores, each tailored to specific project requirements. Throughout this project, we will emphasize the importance of databases in software development, enabling tasks like creating, reading, updating, and deleting data, and providing a strong foundation for managing and accessing data effectively. 


## Learning Objectives
How to create a new MySQL user

How to manage privileges for a user to a database or table

What’s a PRIMARY KEY

What’s a FOREIGN KEY

How to use NOT NULL and UNIQUE constraints

How to retrieve datas from multiple tables in one request

What are subqueries

What are JOIN and UNION

## Comments


```bash

$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```bash


Install MySQL 8.0 on Ubuntu 20.04 LTS

```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

Connect to your MySQL server:

```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
Use “container-on-demand” to run MySQL

*In the container, credentials are root/root

1. Ask for container Ubuntu 20.04

2. Connect via SSH

3. OR connect via the Web terminal

In the container, you should start MySQL before playing with it:

```bash
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```
How to import a SQL dump

```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
<a href="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231018T144048Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=53e7e611e1f84b09e4bd99738fd57cf99b1d7f06cf6d1c3a03049d7d7bb51824">CheatSheet</a>


## Requirments
Allowed editors: vi, vim, emacs

All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)

All your files should end with a new line

All your SQL queries should have a comment just before (i.e. syntax above)

All your files should start by a comment describing the task

All SQL keywords should be in uppercase (SELECT, WHERE…)

A README.md file, at the root of the folder of the project, is mandatory

The length of your files will be tested using wc

