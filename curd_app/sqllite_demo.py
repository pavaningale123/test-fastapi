# to access the data from test.db
import sqlite3  
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#list all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)

#query from first table
cursor.execute("SELECT * FROM employee;")
rows = cursor.fetchall()
print("Data from employees table:", rows)

# for row in rows:
#     print(row)
