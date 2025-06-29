#program to find nCr
import math


def nCr(n,r):
  return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
result = (nCr(n,r))
print(result)