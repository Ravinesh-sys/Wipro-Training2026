import pandas as pd

data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# IT employees
it_employees = df[df["Department"] == "IT"]
print("\nIT Employees:\n", it_employees)

# Average salary
avg_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage salary per department:\n", avg_salary)

# Salary increase by 10%
df["Salary_Adjusted"] = df["Salary"] * 1.10
print("\nFinal DataFrame:\n", df)
