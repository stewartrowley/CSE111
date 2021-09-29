# imports the math tools.
import math

# asking user the number.
items = int(input("Enter the number of items: "))
per_boxes = int(input("Enter the number of items per box: "))

# computes total number of boxes needed.
num_boxes = math.ceil(items / per_boxes)

# displays the number of boxes needed.
print(f"For {items}, packing {per_boxes} items in each box, you will need {num_boxes} boxes.")
