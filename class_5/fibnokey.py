
def fibnokey(num):
  t1 = 0
  t2 = 1

  if num >= 1:
    print(t1)
  if num >= 2:
    print(t2)
  for _ in range(2, num):
    nextTerm = t1 + t2
    t1 = t2
    t2 = nextTerm
    print(nextTerm)

num = int(input("Enter a number: "))
fibnokey(num)