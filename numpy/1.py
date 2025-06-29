import pandas as pd

x=pd.Series([10,20,30])
print(x)
print("_____________")
y=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(y)
print("_____________")
d={1:30,2:40,3:50}
z=pd.Series(d)
z.index = ['a','b','c']
print(z)
print("______________________")
print(x.head(3))
print(x.tail(3))

