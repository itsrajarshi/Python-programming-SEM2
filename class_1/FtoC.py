import math

# Input temperature in Fahrenheit
f = int(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
celsius = (f - 32) * (5.0 / 9.0)

# Print result with two decimal places
print(f"Temperature in Celsius: {celsius:.2f}")