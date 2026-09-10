import numpy as np
import pandas as pd

# Salary data
salary = np.array([
    [2, 4.5, 39000],
    [5, 4.8, 60000],
    [1, 3.5, 25000],
    [7, 4.9, 70000],
    [3, 4.0, 45000]
])

# Salary calculations
print(np.mean(salary[:, 2]))
print(np.max(salary[:, 2]))
print(np.min(salary[:, 2]))

# Performance score average
print(np.mean(salary[:, 1]))

# Find positions where salary is greater than 50000
print(np.where(salary[:, 2] > 50000))

# Find positions where salary is greater than 40000
print(np.where(salary[:, 2] > 40000))

# Find positions where salary is less than 30000
print(np.where(salary[:, 2] < 30000))

# Standard deviation of salary
print(np.std(salary[:, 2]))

# Salary category
salary_category = np.where(
    salary[:, 2] < 50000,
    'Lowest salary',
    'Highest Salary'
)

print(salary_category)

# Create Pandas DataFrame
result = pd.DataFrame(
    salary,
    columns=['Experience', 'Performance Score', 'Salary']
)

print(result)

# Display basic information
print("\nAverage Salary:")
print(result['Salary'].mean())

print("\nHighest Salary:")
print(result['Salary'].max())

print("\nLowest Salary:")
print(result['Salary'].min())

print("\nAverage Performance Score:")
print(result['Performance Score'].mean())

print("\nFinal Data:")
print(result)