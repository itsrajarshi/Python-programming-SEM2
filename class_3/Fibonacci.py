# Input: number of terms
x = int(input("Enter the number of terms in the Fibonacci series: "))

a = 0
b = 1
count = 0

print("Fibonacci series:")

while count < x:
    print(a)
    next_term = a + b
    a = b
    b = next_term
    count += 1
    