# Import required libraries
import pandas as pd
import numpy as np

# Given data (list of dictionaries)
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]

#Convert list to Pandas DataFrame
df = pd.DataFrame(students)

print("Student DataFrame:")
print(df)

#Calculate mean, median, and standard deviation using NumPy
scores = df["score"].to_numpy()

mean_score = np.mean(scores)
median_score = np.median(scores)
std_dev = np.std(scores)

print("\nStatistics:")
print("Mean score:", mean_score)
print("Median score:", median_score)
print("Standard Deviation:", std_dev)

# Add new column 'above_average'
df["above_average"] = df["score"] > mean_score

print("\nUpdated DataFrame with above_average column:")
print(df)
