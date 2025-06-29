#create a list of tuples and replace the last value of all tuples with the value '100'

input_tuples = input()
try:
    list_of_tuples = eval(input_tuples)
except (SyntaxError, NameError):
    exit()

modified_list = [tpl[:-1] + (100,) for tpl in list_of_tuples]

print(modified_list)
