#create two series which stores marks in two subjects then perform addition, substraction, multiplication and division on series objects.
import pandas as pd

# Create two series to store marks in two subjects
subject1_marks = pd.Series([85, 90, 75, 80, 95])
subject2_marks = pd.Series([70, 80, 85, 65, 75])

# Perform addition, subtraction, multiplication, and division
addition_result = subject1_marks + subject2_marks
subtraction_result = subject1_marks - subject2_marks
multiplication_result = subject1_marks * subject2_marks
division_result = subject1_marks / subject2_marks


print(addition_result)
print(subtraction_result)
print(multiplication_result)
print(division_result)

