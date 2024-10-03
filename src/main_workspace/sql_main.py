"""
example simple dp with python and sqlite3
made with the help of chatgpt4
"""

import sqlite3

# 1. Connect to SQLite Database (or create it if it doesn't exist)
conn = sqlite3.connect(
    "example.db"
)  # Creates the database file example.db in the current directory
cursor = conn.cursor()

# 2. Create a new table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL NOT NULL
)
"""
)

# 3. Insert some records (CRUD: Create)
cursor.execute(
    """
INSERT INTO employees (name, position, salary)
VALUES ('Alice', 'Developer', 85000.00)
"""
)
cursor.execute(
    """
INSERT INTO employees (name, position, salary)
VALUES ('Bob', 'Designer', 65000.00)
"""
)
cursor.execute(
    """
INSERT INTO employees (name, position, salary)
VALUES ('Nathan', 'Student', -30000.00)
"""
)
conn.commit()  # Save (commit) the changes

# 4. Query data (CRUD: Read)
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("First entries:")
for row in rows:
    print(row)

# 5. Update a record for Alice (CRUD: Update)
cursor.execute(
    """
UPDATE employees
SET salary = 90000.00
WHERE name = 'Alice'
"""
)
conn.commit()

# 6. Query again to see the updated data
cursor.execute('SELECT * FROM employees WHERE name = "Alice"')
alice_record = cursor.fetchone()
print("\nUpdated record for Alice:")
print(alice_record)

# 7. Delete a record (CRUD: Delete)
cursor.execute(
    """
DELETE FROM employees
WHERE name = 'Bob'
"""
)
conn.commit()

# 8. Query again to see that the deletion worked
cursor.execute("SELECT * FROM employees")
remaining_rows = cursor.fetchall()
print("\nRemaining records after deletion:")
for row in remaining_rows:
    print(row)

# 9. Two different SQL queries
# Query 1: Find all employees with salary > 80000
cursor.execute("SELECT * FROM employees WHERE salary > 80000")
high_salary_employees = cursor.fetchall()
print("\nEmployees with salary greater than 80k:")
for emp in high_salary_employees:
    print(emp)

# Query 2: Count the number of employees
cursor.execute("SELECT COUNT(*) FROM employees")
employee_count = cursor.fetchone()[0]
print(f"\nTotal number of employees: {employee_count}")

# Close the connection
conn.close()
