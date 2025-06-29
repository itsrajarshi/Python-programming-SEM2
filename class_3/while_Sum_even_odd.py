a = int(input("enter a: "))
b = int(input("enter b: "))

S=0
OS=0
i=a
while(i<=b):
  if i%2 == 0:
    S = S + i
  else:
    OS = OS + i
  i=i+1
print(S,OS)

