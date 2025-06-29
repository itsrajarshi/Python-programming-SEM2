# Input a string
text = input("Enter a sentence: ")
words = text.split()
word_count = {}
result = []

# Track repeat count of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 0
    result.append(word_count[word])

print("Repeat count array:", result)