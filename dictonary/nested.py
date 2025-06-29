d={1:{'name':'jay','age':20},2:{'name':'rahul','age':21}}
print(d)
print(d[1]['name'])
print(d[2]['name'])
for i,j in d.items():
  for k in j.items():
    print(k)
