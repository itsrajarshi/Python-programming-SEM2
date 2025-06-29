# Create a dictionary of even numbers (10–20) and their factors
d = {i: [j for j in range(1, i+1) if i % j == 0] for i in range(10, 21) if i % 2 == 0}
print("Even numbers and their factors:")
print(d)