import pandas as pd

students_data = {
    'roll no': list(range(1, 16)),
    'name': [
        'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah',
        'Ivy', 'Jack', 'Kate', 'Liam', 'Mia', 'Noah', 'Olivia'
    ],
    'age': [25, 20, 19, 18, 23, 28, 26, 24, 22, 21, 27, 29, 30, 31, 32],
    'cgpa': [3.5, 3.2, 3.8, 3.9, 3.7, 3.6, 3.4, 3.1, 3.3, 3.0, 3.8, 3.5, 3.2, 9.7, 8.2],
    'branch': [
        'CSE', 'ECE', 'MECH', 'CSE', 'ECE', 'CSE', 'IT', 'CSE', 'IT', 'CSE',
        'CSE', 'IT', 'CSE', 'IT', 'ECE'  # Added 15th branch entry
    ],
    'address': [
        '123 Main St', '456 Elm St', '789 Oak St', '101 Pine St',
        '765 Pune St', '202 Maple St', '789 Oak St', '101 Pine St',
        '202 Maple St', '789 Oak St', '101 Pine St', '202 Maple St',
        '789 Oak St', '101 Pine St', '202 Maple St'
    ],
}

df = pd.DataFrame(students_data)
print("Student DataFrame:\n", df)