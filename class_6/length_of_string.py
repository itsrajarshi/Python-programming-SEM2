# List of strings
d = ['apple', 'sky', 'word']

# Function to get length of a string
def leng(x):
    return len(x)

# Apply 'leng' function to each element in the list
lengths = list(map(leng, d))

# Display the result
print("Lengths of each string:", lengths)