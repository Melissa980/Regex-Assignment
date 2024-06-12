# Question 4 Task 1

import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

tags = []

for description in descriptions:
    if re.search(r'smartphone|phone|tablet|device', description, re.IGNORECASE):
        tags.append('Electronics')
    elif re.search(r't-shirt|shirt|apparel|clothing', description, re.IGNORECASE):
        tags.append('Apparel')
    elif re.search(r'kitchen|cookware|utensil|knife|pan', description, re.IGNORECASE):
        tags.append('Home & Kitchen')
    else:
        tags.append('Other')

print(tags)

