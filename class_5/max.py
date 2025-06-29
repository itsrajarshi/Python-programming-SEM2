def max(a,b,c):
  if a > b and a > c:
    print(a,"is the largest")
  elif b > a and b > c:
    print(b,"is the largest")
  else:
    print(c,"is the largest")
  
a = int(input(""))
b = int(input(""))
c = int(input(""))
max(a,b,c)