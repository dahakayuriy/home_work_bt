#1
# CREATE TABLE original_table (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255),
#     age INTEGER
# );


# INSERT INTO original_table (name, age) VALUES
#     ('John', 25),
#     ('Alice', 30),
#     ('Bob', 22);


# ALTER TABLE original_table RENAME TO renamed_table;


# ALTER TABLE renamed_table ADD COLUMN city VARCHAR(255);


# UPDATE renamed_table SET city = 'New York' WHERE name = 'John';


# DELETE FROM renamed_table WHERE name = 'Bob';


# UPDATE renamed_table SET age = 31 WHERE name = 'Alice';

###########################################################
#2
# -- 1. Displaying first and last names using aliases
# SELECT first_name || ' ' || last_name AS "First name", last_name || ' ' || first_name AS "Last name"
# FROM employees;

# -- 2. Getting a unique department identifier
# SELECT DISTINCT department_id
# FROM employees;

# -- 3. Getting all employee data sorted by last name in descending order
# SELECT * FROM EMPLOYEES
# FROM employees
# ORDER BY last_name DESC;

# -- 4. Getting the name, salary, and pension fund for all employees
# SELECT first_name || ' ' || last_name AS "Name", salary AS "Salary", salary * 0.12 AS "Pension"
# FROM employees;

# -- 5. Getting the maximum and minimum salary
# SELECT MAX(salary) AS "Maximum salary", MIN(salary) AS "Minimum salary"
# FROM employees;

# -- 6. Getting the monthly salary of each employee
# SELECT first_name || ' ' || last_name AS "Name", salary / 12.0 AS "Monthly salary"
# FROM employees;