def convert(tup):
    return int(''.join(str(d) for d in tup))

# Example usage
digits = (1, 2, 3, 4)
result = convert(digits)
print("Converted integer:", result)