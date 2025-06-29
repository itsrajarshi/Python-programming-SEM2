# Input cost price and selling price
CP = int(input("Enter Cost Price (CP): "))
SP = int(input("Enter Selling Price (SP): "))

# Calculate difference and percentage
dif = SP - CP
percentage = (dif / CP) * 100

# Output result
if percentage > 0:
    print(f"Profit of {percentage:.2f}%")
elif percentage < 0:
    print(f"Loss of {-percentage:.2f}%")
else:
    print("No profit, no loss.")