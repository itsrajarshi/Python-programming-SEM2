#create a dictonary of cubes of odd numbers in the range 1 to 10

d={}
for i in range(1,11):
  if i%2 == 1:
    d[i] = i*i*i
print(d)