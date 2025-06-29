import math


def factorial(x):
  if x == 0:
    print("0! = 1")
  else:
    math.factorial(x)
    print(x, "! =", math.factorial(x))
x = int(input("Enter a number: "))
factorial(x)