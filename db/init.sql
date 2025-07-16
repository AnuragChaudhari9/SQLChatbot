USE chatbot_db;

CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(100),
    salary DECIMAL(10, 2)
);

INSERT INTO employees (name, role, salary) VALUES
('Alice', 'Data Scientist', 100000),
('Bob', 'ML Engineer', 95000),
('Charlie', 'Analyst', 80000);
