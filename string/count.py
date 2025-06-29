#count all the letters and digits and special symbols in a given string.
x = input("")
count = sum(c.isdigit() for c in x)
c_char = sum(c.isalpha() for c in x)
c_special = sum(c.isidentifier() for c in x)
print(count)
print(c_char)
print(c_special)