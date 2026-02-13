import pandas as pd

# Read Excel file
df = pd.read_excel("sales_data.xlsx", sheet_name="2025")

# Add new column Total = Quantity * Price
df["Total"] = df["Quantity"] * df["Price"]

# Save to new Excel file
df.to_excel("sales_summary.xlsx", index=False)

print("File saved successfully!")
