import pandas as pd

employees_by_department = {
    'HR': ['Alice', 'Bob', 'Charlie'],
    'Finance': ['David', 'Eve', None],
    'IT': ['Frank', 'Grace', None],
    'Marketing': ['Hannah', 'Ivy', 'Jack']
}

print("About to create a DataFrame for employee assignments.\n")
df = pd.DataFrame(employees_by_department)
print("Employee DataFrame:")
print(df)