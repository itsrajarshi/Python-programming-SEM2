char = input("Enter a letter: ")

if char.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")