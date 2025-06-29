#read a tuple and print it in reversed order.

a = input()
tuple1 = tuple(a.split(','))
revtuple1 = tuple1[::-1]
print("orignal tuple :",tuple1)
print("Reversed tuple :",revtuple1)