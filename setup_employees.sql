DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary INT,
    joining_date DATE,
    designation VARCHAR(50),
    location VARCHAR(50),
    experience FLOAT
);

INSERT INTO employees (id, name, department, salary, joining_date, designation, location, experience) VALUES
(1, 'Alice', 'HR', 50000, '2019-03-15', 'HR Manager', 'Mumbai', 5.0),
(2, 'Bob', 'Engineering', 75000, '2020-06-01', 'Software Engineer', 'Bangalore', 4.2),
(3, 'Charlie', 'Sales', 60000, '2021-01-20', 'Sales Executive', 'Delhi', 3.5),
(4, 'David', 'Engineering', 85000, '2018-10-05', 'Senior Engineer', 'Hyderabad', 6.1),
(5, 'Eva', 'HR', 52000, '2022-02-12', 'HR Executive', 'Pune', 2.0),
(6, 'Fiona', 'Marketing', 62000, '2020-11-01', 'Marketing Manager', 'Mumbai', 4.8),
(7, 'George', 'Engineering', 85000, '2017-04-10', 'Tech Lead', 'Bangalore', 7.2),
(8, 'Hina', 'Sales', 59000, '2021-08-25', 'Sales Associate', 'Delhi', 3.0),
(9, 'Ishaan', 'Marketing', 70000, '2019-12-15', 'Content Strategist', 'Chennai', 5.6),
(10, 'Jaya', 'HR', 54000, '2023-01-03', 'Recruiter', 'Pune', 1.1),
(11, 'Kevin', 'Sales', 85000, '2016-09-12', 'Sales Manager', 'Delhi', 8.0),
(12, 'Leela', 'Finance', 61000, '2020-03-09', 'Accountant', 'Mumbai', 3.9),
(13, 'Manav', 'Finance', 64000, '2019-07-27', 'Financial Analyst', 'Ahmedabad', 5.2),
(14, 'Nina', 'Engineering', 88000, '2015-05-18', 'Engineering Manager', 'Bangalore', 9.5),
(15, 'Om', 'Engineering', 88000, '2016-02-29', 'Engineering Manager', 'Bangalore', 9.0);