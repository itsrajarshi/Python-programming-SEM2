x1 = int(input("Enter the first number (x1): "))
x2 = int(input("Enter the second number (x2): "))

if x1 > x2:
    print("Maximum number is:", x1)
elif x2 > x1:
    print("Maximum number is:", x2)
else:
    print("Both numbers are equal.")