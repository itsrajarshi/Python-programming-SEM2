#find sum and average of the digits present in the string.
x = input("")
sum = 0
for i in x:
    sum += int(i)
print("sum of the digits",sum)
print("avg of the digits",sum/len(x))
