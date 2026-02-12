import pandas as pd
import numpy as np

# Load CSV file
df = pd.read_csv("sales.csv")

print("Original Data:\n")
print(df)

# Add Total column
df["Total"] = df["Quantity"] * df["Price"]

print("\nData with Total column:\n")
print(df)

# NumPy calculations
total_sales = np.sum(df["Total"])
avg_sales = np.mean(df["Total"])
std_sales = np.std(df["Total"])

print("\nSales Analysis:")
print("Total Sales =", total_sales)
print("Average Sales =", avg_sales)
print("Standard Deviation =", std_sales)

# Best selling product
best_product = df.groupby("Product")["Quantity"].sum().idxmax()
best_qty = df.groupby("Product")["Quantity"].sum().max()

print("\nBest Selling Product:")
print(best_product, "Sold:", best_qty)
