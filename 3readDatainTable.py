import sqlite3

def read_students():
    # Connect to the existing database
    conn = sqlite3.connect('databaseFile.db')
    cursor = conn.cursor()
    
    # Retrieve all students from the student_info table
    cursor.execute('SELECT * FROM student_info')
    students = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    # Print each student
    for student in students:
        print(f"Student ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}")

# Example usage
if __name__ == "__main__":
    read_students()
