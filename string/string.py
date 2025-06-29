x = input("Enter a string: ")

if len(x) >= 2:
    result = x[:1] + x[(len(x) // 2) - 1] + x[-1:]
    print("Result:", result)
else:
    print("String too short to process.")