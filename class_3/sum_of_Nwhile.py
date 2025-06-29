# Input a positive integer
n = int(input("Enter a positive integer (n): "))

# Initialize sum and counter
s = 0
i = 1

# Sum natural numbers using while loop
while i <= n:
    s += i
    i += 1

# Display the result
print(f"Sum of first {n} natural numbers is {s}")