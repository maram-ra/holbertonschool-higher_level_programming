# SQL - Introduction

## Description

This project is part of the Holberton School curriculum and serves as an introduction to databases and SQL using MySQL 8.0. It focuses on basic SQL statements (DDL and DML), data manipulation, and querying.

All tasks are solved with SQL scripts and tested via CLI using `mysql` command-line client.

---

## Learning Objectives

- Understand what a database and a relational database are
- Know what SQL stands for and what MySQL is
- How to:
  - Create and delete databases and tables
  - Use DDL and DML statements
  - SELECT data from tables with filters, ordering, and limits
  - INSERT, UPDATE, DELETE records
  - Use functions and subqueries
  - Avoid showing empty or invalid data

---

## Environment

- OS: Ubuntu 20.04 LTS
- MySQL: 8.0.25
- CLI usage only
- All scripts end with a new line and are commented
- Editors: `vi`, `vim`, `emacs`

---

## Files and Tasks

| File                          | Description                                         |
|-------------------------------|-----------------------------------------------------|
| 0-list_databases.sql          | Lists all databases                                 |
| 1-create_database_if_missing.sql | Creates `hbtn_0c_0` if it doesn't exist            |
| 2-remove_database.sql         | Deletes `hbtn_0c_0` if it exists                    |
| 3-list_tables.sql             | Lists all tables from a given DB                    |
| 4-first_table.sql             | Creates `first_table` with `id` and `name`         |
| 5-full_table.sql              | Prints full CREATE statement of `first_table`      |
| 6-list_values.sql             | Lists all rows from `first_table`                  |
| 7-insert_value.sql            | Inserts a row with `id = 89`, `name = Best School` |
| 8-count_89.sql                | Counts rows with `id = 89`                         |
| 9-full_creation.sql           | Creates `second_table` and inserts multiple rows   |
| 10-top_score.sql              | Lists all records ordered by `score` descending    |
| 11-best_score.sql             | Lists all records with `score >= 10`               |
| 12-no_cheating.sql            | Updates Bob’s score to 10 using name only          |
| 13-change_class.sql           | Deletes all rows with `score <= 5`                 |
| 14-average.sql                | Displays average score                             |
| 15-groups.sql                 | Counts how many records per score                  |
| 16-no_link.sql                | Lists only records with non-empty `name`           |

---

