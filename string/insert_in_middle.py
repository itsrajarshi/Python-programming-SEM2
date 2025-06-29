# Input the original and middle strings
x = input("Enter the original string: ")
middle = input("Enter the string to insert in the middle: ")

# Find the middle index and insert the string
middle_index = len(x) // 2
new_str = x[:middle_index] + middle + x[middle_index:]

# Output the result
print("Resulting string:", new_str)