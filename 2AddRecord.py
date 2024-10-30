import sqlite3

def add_student(student_id, first_name, last_name):
    # Connect to the existing database
    conn = sqlite3.connect('databaseFile.db')
    cursor = conn.cursor()
    
    # Insert a new student into the student_info table
    cursor.execute('''
        INSERT INTO student_info (student_id, first_name, last_name)
        VALUES (?, ?, ?)
    ''', (student_id, first_name, last_name))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(f"Student {first_name} {last_name} added successfully.")

# Example usage
add_student(1, 'John', 'Doe')
add_student(2, 'Jane', 'Smith')
add_student(3, 'Alice', 'Johnson')
