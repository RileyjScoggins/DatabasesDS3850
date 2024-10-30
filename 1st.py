import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('DatabaseFile.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table named student_info
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_info (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
