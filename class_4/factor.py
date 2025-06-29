# Input a number
x = int(input("Enter a number to find its factors: "))

# Print all factors of the number
print(f"Factors of {x} are:")
for i in range(1, x + 1):
    if x % i == 0:
        print(i)