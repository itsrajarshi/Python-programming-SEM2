# Input a number
num = int(input("Enter a number: "))
sum = 0

# Sum the digits
while num != 0:
    digit = num % 10
    sum += digit
    num = num // 10  # Use integer division

# Display the result
print(f"Sum of digits: {sum}")