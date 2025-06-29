#create a dataframe with attributes roll no, name,age,cgpa,branch and address with min 
#of 15 rows.

import pandas as pd

students_data = {
    'roll no': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'name': [
        'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah',
        'Ivy', 'Jack', 'Kate', 'Liam', 'Mia', 'Noah', 'Olivia'
    ],
    'age': [25, 20, 19, 18, 23, 28, 26, 24, 22, 21, 27, 29, 30, 31, 32],
    'cgpa': [
        3.5, 3.2, 3.8, 3.9, 3.7, 3.6, 3.4, 3.1, 3.3, 3.0, 3.8, 3.5, 3.2, 9.7,
        8.2
    ],
    'branch': [
        'CSE', 'ECE', 'MECH', 'CSE', 'ECE', 'CSE', 'IT', 'CSE', 'IT', 'CSE',
        'CSE', 'IT', 'CSE', 'IT', 'CSE'
    ],
    'address': [
        '123 Main St', '456 Elm St', '789 Oak St', '101 Pine St',
        '765 Pune St', '202 Maple St', '789 Oak St', '101 Pine St',
        '202 Maple St', '789 Oak St', '101 Pine St', '202 Maple St',
        '789 Oak St', '101 Pine St', '202 Maple St'
    ],
}

df = pd.DataFrame(students_data)
print(df)

print("_____________________________________")

print("display name,age,cgpa of all students")

print("_____________________________________")

print(df[['name', 'age', 'cgpa']])

print("_____________________________________")

print("display 4th student details")

print("_____________________________________")

print(df.loc[3])

print("_____________________________________")

print("display 2nd, 8th and 12th student details")

print("_____________________________________")

print(df.loc[[1, 7, 11]])

print("_____________________________________")

print("display the topper cgpa in the class")

print(df.loc[df['cgpa'].idxmax()])

print("_____________________________________")

print("display the student name who are in the age 20-25")

print("_____________________________________")

print(df.loc[df['age'].between(20, 25)])

print("_____________________________________")

print("display the first 10 toppers of the class")
dft=df.sort_values('cgpa',ascending=False)
print(dft.iloc[0:9:])

print("_____________________________________")

print("print the slow learners in the class")
print("_____________________________________")
dfs=df.sort_values('cgpa',ascending=True)
print(dfs.iloc[0:3:])

print("_____________________________________")

print("display the students who are in the CSE branch and adress of 123 Main St")
print("_____________________________________")
print(df.loc[(df['branch'] == 'CSE') & (df['address'] == '123 Main St')])
print(df.loc[df['branch'] == 'CSE'])

print("_____________________________________")

print("print names of students from young to older age")

print(df.sort_values(by='age'))

print("_____________________________________")

print("4th student in each branch")

print(df.groupby('branch').nth(3))

print("_____________________________________")