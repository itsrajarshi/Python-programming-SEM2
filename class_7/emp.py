import pandas as pd

employee_data = {
    'Employee Number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Salary': [50000, 60000, 70000, 80000, 90000, 75000, 65000, 55000, 72000, 68000]
}
employee_df = pd.DataFrame(employee_data)

department_data = {
    'Department Number': [101, 102, 103, 104],
    'Department Name': ['HR', 'Finance', 'IT', 'Marketing'],
    'Location': ['New York', 'San Francisco', 'Seattle', 'Los Angeles']
}
department_df = pd.DataFrame(department_data)

employee_department_df = pd.merge(employee_df, department_df, left_index=True, right_index=True)
employee_department_df = employee_department_df[['Name', 'Employee Number', 'Salary', 'Department Name']]

print(employee_department_df)