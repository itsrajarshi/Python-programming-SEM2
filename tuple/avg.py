def average(tuples):
    return [sum(t) / len(t) for t in tuples]

# List of 4-element tuples
data = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)]

# Compute average values
print("Average values:", average(data))