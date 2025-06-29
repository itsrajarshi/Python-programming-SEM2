import numpy as np

a = np.array([1, 3, 5, 7])
b = [True,4,6.8,5]
c = np.array([[10,20],[30,40],[50,60]])
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(a[1])
print(a[-2])
print(a[2:4])
print(a[-2:])

print("_____________")
mix=np.array(b)
print(mix)

print("_____________")
print(c[2])
print(c[2,0])
print(c[1,-1])
print(c[1,1:2])

print("_____________")
print(d[1,0,1])
print(d[-1,-1,-1])

