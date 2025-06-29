# Tuple of tuples
t = ((1, 2), (3, 4), (5, 6))

# Element-wise sum using zip and sum
result = tuple(sum(x) for x in zip(*t))

# Display result
print("Element-wise sum:", result)