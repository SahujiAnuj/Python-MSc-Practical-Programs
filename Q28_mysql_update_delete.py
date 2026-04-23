# Program 28: Update and Delete Records in MySQL

import mysql.connector

try:
    # 1. Connect to Database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college_db"
    )
    cursor = db.cursor()

    # 2. UPDATE - Change data
    # Updating marks for a specific student (Roll No 101)
    sql_update = "UPDATE students SET marks = %s WHERE roll_no = %s"
    val_update = (98.0, 101)
    
    cursor.execute(sql_update, val_update)
    db.commit() # Must commit for UPDATES
    print(cursor.rowcount, "record(s) updated.")

    # 3. DELETE - Remove data
    # Deleting a student record (Roll No 102)
    sql_delete = "DELETE FROM students WHERE roll_no = %s"
    val_delete = (102,) # Tuple with one element needs a comma
    
    cursor.execute(sql_delete, val_delete)
    db.commit() # Must commit for DELETES
    print(cursor.rowcount, "record(s) deleted.")

    cursor.close()
    db.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
