import pandas as pd

file = input("csv/EX.csv")
df1 = pd.read_csv(file)

# Sort by salary in ascending order and keep only top 4
df1 = df1.sort_values(by='Salary', ascending=True)
print("Four employees with the lowest salaries:")
print(df1.iloc[0:4, [0, 1, 2]])