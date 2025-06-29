#read a tuple and find repeated elements in it.

def find_repeated_elements(a):
  repeated_elements = []
  for i in a:
    if a.count(i) > 1 and i not in repeated_elements:
      repeated_elements.append(i)
  return repeated_elements

a = input()
a = tuple(a.split(","))
print(find_repeated_elements(a))
