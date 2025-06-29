# Program to count the number of digits in a given string
x = input("Enter a string: ")
count = sum(c.isdigit() for c in x)
print(f"Number of digits in the string: {count}")