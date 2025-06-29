year = int(input("enter a number: "))
if (year % 400) == 0:
  print("the given year is a leap year")
elif (year % 100) == 0:
  print("the given year is not a leap year")
elif (year % 4) == 0:
  print("the given year is a leap year")
else:
  print("the given year is not a leap year")
