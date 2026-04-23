# Program 26: Python to MySQL Connection (Create & Insert)

import mysql.connector

# 1. Establish Connection
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college_db"
    )
    cursor = db.cursor()
    print("Connected to MySQL Successfully!")

    # 2. Create Table
    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute("""
        CREATE TABLE students (
            roll_no INT PRIMARY KEY,
            name VARCHAR(50),
            marks FLOAT
        )
    """)
    print("Table 'students' created.")

    # 3. Insert a Record
    sql = "INSERT INTO students (roll_no, name, marks) VALUES (%s, %s, %s)"
    val = (101, "Anuj", 95.5)
    
    cursor.execute(sql, val)
    db.commit() # Important: Save changes to the database
    
    print(cursor.rowcount, "record inserted.")

    # 4. Close Connection
    cursor.close()
    db.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
