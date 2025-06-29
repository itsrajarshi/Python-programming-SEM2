# Create a dictionary with radius as key and [area, circumference] as value
d = {}
for r in range(1, 6):  # Example: radii from 1 to 5
    area = round(3.14 * r * r, 2)
    circumference = round(2 * 3.14 * r, 2)
    d[r] = [area, circumference]

print("Radius → [Area, Circumference]:")
print(d)