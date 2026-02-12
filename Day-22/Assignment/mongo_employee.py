from pymongo import MongoClient

# connect to mongodb
client = MongoClient("mongodb://localhost:27017/")

# database
db = client["company_db"]

# collection
collection = db["employees"]

print("Connected to MongoDB")

# ------------------------------
# 1. Insert new employee
# ------------------------------
employee = {
    "name": "Amit",
    "department": "IT",
    "salary": 55000
}

collection.insert_one(employee)
print("Employee inserted")

# ------------------------------
# 2. Find all IT employees
# ------------------------------
print("\nEmployees in IT department:\n")

it_employees = collection.find({"department": "IT"})

for emp in it_employees:
    print(emp)

# ------------------------------
# 3. Update salary by name
# ------------------------------
collection.update_one(
    {"name": "Amit"},      # employee name
    {"$set": {"salary": 65000}}   # new salary
)

print("\nSalary updated")

# show final data
print("\nFinal data:\n")
for emp in collection.find():
    print(emp)
