#create a dictonary to store name,age,address and qualifications of five employees convert it into a dataframe and print it.
import pandas as pd

employees_data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [30, 35, 40, 45, 50],
    'address': ['123 Main St', '456 Elm St', '789 Oak St', '101 Pine St', '202 Maple St'],
    'qualifications': ['B.Tech', 'Master', 'PhD', 'Bachelor', 'Master']
}

employees_df = pd.DataFrame(employees_data)
print(employees_df)