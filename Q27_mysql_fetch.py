# Program 27: Retrieve and Display Records from MySQL

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

    # 2. Fetch All Records (The most common way)
    print("--- All Students ---")
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall() # Returns a list of tuples
    
    for row in rows:
        print(f"Roll No: {row[0]} | Name: {row[1]} | Marks: {row[2]}")

    # 3. Fetch Single Record (Using WHERE)
    print("\n--- Search Result (Roll No 101) ---")
    cursor.execute("SELECT * FROM students WHERE roll_no = 101")
    single_row = cursor.fetchone()
    if single_row:
        print(single_row)

    # 4. Fetch First 2 Records (fetchmany)
    print("\n--- Fetching first 2 records ---")
    cursor.execute("SELECT name FROM students")
    result = cursor.fetchmany(2)
    print(result)

    cursor.close()
    db.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
