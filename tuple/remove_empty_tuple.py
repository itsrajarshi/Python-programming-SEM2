# Create a list of tuples including some empty ones
list1 = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (), (), ()]

# Remove all empty tuples
list1 = [t for t in list1 if t]

# Display the result
print("List after removing empty tuples:", list1)