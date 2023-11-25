import pymysql

# Establish a connection to MySQL
conn = pymysql.connect(host="localhost", user="root", password="root123")

# Create a cursor
cursor = conn.cursor()

# Create the 'Employee' database
cursor.execute("CREATE DATABASE IF NOT EXISTS Employee")

# Switch to the 'Employee' database
cursor.execute("USE Employee")

# Create the 'EmpInfo' table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS EmpInfo (Emp_NO int NOT NULL, Emp_Name varchar(50), Salary int, Address varchar(100), Role_Type varchar(50))")

# Insert data into the table (fix the typographical error)
cursor.execute("INSERT INTO EmpInfo VALUES (01, 'Akansha', 35000, 'Wagholi', 'Biomedical Engineer')")
cursor.execute("INSERT INTO EmpInfo VALUES (02, 'Devi', 25500, 'Kalyani Nagar', 'Computational Biologist')")
cursor.execute("INSERT INTO EmpInfo VALUES (03, 'Apurva', 28000, 'Karve Nagar', 'Biotechnologist')")
cursor.execute("INSERT INTO EmpInfo VALUES (04, 'Meher', 30000, 'Wagholi-BJS', 'Bioinformatician')")

# Commit the changes for the initial data insertion
conn.commit()

# Select and display data
cursor.execute("SELECT * FROM EmpInfo")
Emp = cursor.fetchall()
print("Initial data fetching:")
for i in Emp:
    print(i)

print("-------------------------------------------------")
# Alter the table to add columns 'Email' and 'Age'
cursor.execute("ALTER TABLE EmpInfo ADD COLUMN Email varchar(255)")
cursor.execute("ALTER TABLE EmpInfo ADD COLUMN Age int")

# Insert 'Email' and 'Age' data
cursor.execute("UPDATE EmpInfo SET Email = 'akansha@gmail.com', Age = 22 WHERE Emp_NO = 01")
cursor.execute("UPDATE EmpInfo SET Email = 'devi@gmail.com', Age = 22 WHERE Emp_NO = 02")
cursor.execute("UPDATE EmpInfo SET Email = 'apurva@gmail.com', Age = 23 WHERE Emp_NO = 03")
cursor.execute("UPDATE EmpInfo SET Email = 'meher@gmail.com', Age = 22 WHERE Emp_NO = 04")

# Commit the changes for adding 'Email' and 'Age'
conn.commit()

# Select and display data after adding 'Email' and 'Age'
cursor.execute("SELECT * FROM EmpInfo")
Emp = cursor.fetchall()

print("Data aftering altering the table:")
for i in Emp:
    print(i)

print("-------------------------------------------------")

# Delete the 'Age' column
cursor.execute("ALTER TABLE EmpInfo DROP COLUMN Age")

# Commit the changes for deleting 'Age'
conn.commit()

# Select and display data after deleting 'Age'
cursor.execute("SELECT * FROM EmpInfo")
Emp = cursor.fetchall()
print("Data after deleting:")
for i in Emp:
    print(i)

print("-------------------------------------------------")
# Close the cursor and the connection
cursor.close()
conn.close()
