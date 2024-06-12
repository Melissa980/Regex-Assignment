# Question 3 Task 1

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
key = "Occupation"
occupation = re.search(rf"{key}: ([^;]+)", text).group(1)
print(occupation)
