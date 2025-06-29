x1 = int(input("Enter first number (x1): "))
x2 = int(input("Enter second number (x2): "))
x3 = int(input("Enter third number (x3): "))

# Determine the minimum
if x1 <= x2 and x1 <= x3:
    print("The minimum of the three numbers is:", x1)
elif x2 <= x1 and x2 <= x3:
    print("The minimum of the three numbers is:", x2)
else:
    print("The minimum of the three numbers is:", x3)