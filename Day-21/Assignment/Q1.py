import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

# Matplotlib Line Chart
plt.figure(figsize=(8,5))
plt.plot(months, sales, marker='o', color='blue')

plt.title("Monthly Sales Line Chart")
plt.xlabel("Months")
plt.ylabel("Sales (in Rs)")
plt.grid(True)

plt.show()

# Seaborn Bar Plot
plt.figure(figsize=(8,5))
sns.barplot(x=months, y=sales)

plt.title("Monthly Sales Bar Plot")
plt.xlabel("Months")
plt.ylabel("Sales (in Rs)")
plt.grid(True)

plt.show()
