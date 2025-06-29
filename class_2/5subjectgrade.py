# Input scores
x1 = int(input("Enter marks for subject 1: "))
x2 = int(input("Enter marks for subject 2: "))
x3 = int(input("Enter marks for subject 3: "))
x4 = int(input("Enter marks for subject 4: "))
x5 = int(input("Enter marks for subject 5: "))

# Calculate average
total = x1 + x2 + x3 + x4 + x5
average = total / 5

# Grade evaluation
if 90 <= average <= 100:
    print("O grade")
elif 80 <= average < 90:
    print("A+ grade")
elif 70 <= average < 80:
    print("A grade")
elif 60 <= average < 70:
    print("B grade")
elif 50 <= average < 60:
    print("C grade")
elif 40 <= average < 50:
    print("D grade")
elif 30 <= average < 40:
    print("E grade")
elif 20 <= average < 30:
    print("F grade")
else:
    print("Fail")