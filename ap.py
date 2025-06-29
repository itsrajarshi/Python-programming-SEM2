def replace_alphabets(input_string):
  output_string = ""
  for char in input_string:
      if char.isalpha():
          if char.lower() == 'z':
              next_char = 'a'
          else:
              next_char = chr(ord(char) + 1)
              if next_char.lower() in 'aeiou':
                  next_char = chr(ord(next_char) + 1)
      else:
          next_char = char
      output_string += next_char

  return output_string

input_text = input()
output_text = replace_alphabets(input_text)
print(output_text)
