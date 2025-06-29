#create a nested list which consists of name and cgpa of ten students convert it into a dataframe and display the last five records in it.

import pandas as pd

# Create a nested list of name and cgpa for ten students
student_data = [
    ['Alice', 3.5],
    ['Bob', 3.2],
    ['Charlie', 3.8],
    ['David', 3.9],
    ['Eve', 3.7],
    ['Frank', 3.6],
    ['Grace', 3.4],
    ['Hannah', 3.1],
    ['Ivy', 3.3],
    ['Jack', 3.0]
]

# Convert the nested list into a DataFrame
student_df = pd.DataFrame(student_data, columns=['Name', 'CGPA'], index=[1,2,3,4,5,6,7,8,9,10])

# Display the last five records of the DataFrame
print(student_df.tail(5))