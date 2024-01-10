# -- 1. First name, last name, department number, and department name for each employee
# SELECT first_name, last_name, department_id, department_name
# FROM employees
# JOIN departments ON employees.department_id = departments.department_id;

# -- 2. First name, last name, department, city, and province for each employee
# SELECT first_name, last_name, department_name, city, state_province
# FROM employees
# JOIN departments ON employees.department_id = departments.department_id
# JOIN locations ON departments.location_id = locations.location_id;

# -- 3. First name, last name, department number, and department name for all employees for departments 80 or 40
# SELECT first_name, last_name, department_id, department_name
# FROM employees
# JOIN departments ON employees.department_id = departments.department_id
# WHERE department_id IN (40, 80);

# -- 4. All departments, including those without any employees
# SELECT * FROM DEPARTMENTS
# FROM departments
# LEFT JOIN employees ON departments.department_id = employees.department_id;

# -- 5. Names of all employees, including the name of their manager
# SELECT e1.first_name || ' ' || e1.last_name AS "Employee", e2.first_name || ' ' || e2.last_name AS "Manager"
# FROM employees e1
# LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;

# -- 6. Job title, employee's full name and the difference between the maximum salary for this position and the employee's salary
# SELECT job_title, first_name || ' ' || last_name AS "Full name",
#        salary - MAX(salary) OVER (PARTITION BY job_id) AS "Salary difference"
# FROM employees;

# -- 7. Job title and average salary of employees
# SELECT job_title, AVG(salary) AS "Average salary"
# FROM employees
# GROUP BY job_title;

# -- 8. Full name and salary of employees working in any department located in London
# SELECT first_name || ' ' || last_name AS "Full name", salary
# FROM employees
# JOIN departments ON employees.department_id = departments.department_id
# JOIN locations ON departments.location_id = locations.location_id
# WHERE city = 'London';

# -- 9. Department name and number of employees in each department
# SELECT department_name, COUNT(employee_id) AS "Number of employees"
# FROM employees
# JOIN departments ON employees.department_id = departments.department_id
# GROUP BY department_name;