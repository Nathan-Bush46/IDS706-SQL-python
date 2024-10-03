import sqlite3


# note made with help of chatgpt
def test_sqlite_operations():
    conn = sqlite3.connect(
        ":memory:"
    )  # as we are just testing the opperations makes a new table in memery to test them on
    cursor = conn.cursor()

    # Test 2: Create a new table
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
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='employees'"
    )
    assert cursor.fetchone() is not None, "Table 'employees' should exist"

    # Test 3: Insert records
    cursor.execute(
        "INSERT INTO employees (name, position, salary) VALUES ('Alice', 'Developer', 85000.00)"
    )
    cursor.execute(
        "INSERT INTO employees (name, position, salary) VALUES ('Bob', 'Designer', 65000.00)"
    )
    cursor.execute(
        "INSERT INTO employees (name, position, salary) VALUES ('Nathan', 'Student', -30000.00)"
    )
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM employees")
    assert cursor.fetchone()[0] == 3, "There should be 3 records in the employees table"

    # Test 4: Query data
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    assert len(rows) == 3, "Query should return 3 rows"
    assert rows[0][1] == "Alice", "First row should be Alice"

    # Test 5: Update a record
    cursor.execute("UPDATE employees SET salary = 90000.00 WHERE name = 'Alice'")
    conn.commit()
    cursor.execute("SELECT salary FROM employees WHERE name = 'Alice'")
    assert (
        cursor.fetchone()[0] == 90000.00
    ), "Alice's salary should be updated to 90000.00"

    # Test 6: Query updated data
    cursor.execute('SELECT * FROM employees WHERE name = "Alice"')
    alice_record = cursor.fetchone()
    assert alice_record[3] == 90000.00, "Alice's updated salary should be 90000.00"

    # Test 7: Delete a record
    cursor.execute("DELETE FROM employees WHERE name = 'Bob'")
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM employees")
    assert cursor.fetchone()[0] == 2, "There should be 2 records after deletion"

    # Test 8: Query after deletion
    cursor.execute("SELECT * FROM employees")
    remaining_rows = cursor.fetchall()
    assert len(remaining_rows) == 2, "There should be 2 remaining records"
    assert all(
        row[1] != "Bob" for row in remaining_rows
    ), "Bob should not be in the remaining records"

    # Test 9: Additional SQL queries
    cursor.execute("SELECT * FROM employees WHERE salary > 80000")
    high_salary_employees = cursor.fetchall()
    assert (
        len(high_salary_employees) == 1
    ), "There should be 1 employee with salary > 80000"
    assert (
        high_salary_employees[0][1] == "Alice"
    ), "The high salary employee should be Alice"

    cursor.execute("SELECT COUNT(*) FROM employees")
    employee_count = cursor.fetchone()[0]
    assert employee_count == 2, "The total number of employees should be 2"

    conn.close()
