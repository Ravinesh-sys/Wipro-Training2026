import mysql.connector

# connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # if you set mysql password write here
    database="feb2026"   # your database name
)

cursor = db.cursor()

print("Connected successfully")

# 1️⃣ Fetch employees with salary > 50000
print("\nEmployees with salary > 50000:\n")

cursor.execute("SELECT * FROM employees WHERE salary > 50000")
result = cursor.fetchall()

for row in result:
    print(row)

# Insert new employee
print("\nInserting new employee...\n")

insert_query = "INSERT INTO employees(name,department,salary) VALUES (%s,%s,%s)"
data = ("Rahul", "IT", 65000)

cursor.execute(insert_query, data)
db.commit()

print("New employee inserted")

# Update salary by 10%
print("\nUpdating salary by 10% for Rahul...\n")

update_query = "UPDATE employees SET salary = salary + (salary*0.10) WHERE name='Rahul'"
cursor.execute(update_query)
db.commit()

print("Salary updated")

# check final table
print("\nFinal Table:\n")
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

db.close()
