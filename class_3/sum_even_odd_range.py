# Input range start and end
a = int(input("Enter start of range (a): "))
b = int(input("Enter end of range (b): "))

even_sum = 0
odd_sum = 0

# Calculate sums
for i in range(a, b + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

# Display results
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")