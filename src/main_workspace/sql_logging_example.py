"""
example simple dp_logger with python and sqlite3
made with the help of chatgpt4
"""

import sqlite3
import datetime


# Set up main database connection
conn = sqlite3.connect("main_database.db")
cursor = conn.cursor()

# Set up logging database connection
log_conn = sqlite3.connect("log_database.db")
log_cursor = log_conn.cursor()

# Create a table for logs if it doesn't exist
log_cursor.execute(
    """
CREATE TABLE IF NOT EXISTS operation_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operation TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
"""
)
log_conn.commit()


def log_operation(operation):
    """Log a successful operation to the log database"""
    timestamp = datetime.datetime.now().isoformat()
    log_cursor.execute(
        "INSERT INTO operation_logs (operation, timestamp) VALUES (?, ?)",
        (operation, timestamp),
    )
    log_conn.commit()


# Example database operations
def create_table():
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL
    )
    """
    )
    conn.commit()
    log_operation("Created employees table")


def insert_employee(name, position):
    cursor.execute(
        "INSERT INTO employees (name, position) VALUES (?, ?)", (name, position)
    )
    conn.commit()
    log_operation(f"Inserted employee: {name}, {position}")


def update_employee(employee_id, new_position):
    cursor.execute(
        "UPDATE employees SET position = ? WHERE id = ?", (new_position, employee_id)
    )
    conn.commit()
    log_operation(f"Updated employee ID {employee_id} to position: {new_position}")


# Perform some operations
create_table()
insert_employee("Alice", "Developer")
insert_employee("Bob", "Designer")
update_employee(1, "Senior Developer")

# Query the log database to see the logged operations
log_cursor.execute("SELECT * FROM operation_logs")
logs = log_cursor.fetchall()
print("Operation Logs:")
for log in logs:
    print(log)

# Close connections
conn.close()
log_conn.close()
