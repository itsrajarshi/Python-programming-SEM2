import re

def clean_string(old_string):
    # Remove selected special characters using regex
    new_string = re.sub(r'[”‘l;:!~@#$%^`&*()_+–={}\[\]]', '', old_string)

    # Remove digits
    cleaned = ''.join(char for char in new_string if not char.isdigit())

    return cleaned

# Input and output
old_string = input("Enter a string: ")
result = clean_string(old_string)
print("Cleaned string:", result)