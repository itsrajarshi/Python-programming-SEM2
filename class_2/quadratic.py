import math
import cmath  # for complex number support

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

# Calculate discriminant
discriminant = (b**2) - (4 * a * c)

# Use cmath.sqrt to handle negative roots too
sqrt_val = cmath.sqrt(discriminant)

# Calculate roots
o1 = (-b + sqrt_val) / (2 * a)
o2 = (-b - sqrt_val) / (2 * a)

print("The roots are:")
print(o1)
print(o2)