# Procedural Programming
# def main():
#     numbers = [87, 95, 72, 92, 95, 88, 84]
#     total = 0
#     for x in numbers:
#         total += x
#         average = total / len(numbers)
#         print(average)

# Declaritive Programming
# SELECT AVG(numbers) FROM table;   
   
# Functional Programming
from functools import reduce

def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    func_add = lambda a, b: a + b
    total = reduce(func_add, numbers)
    average =  total / len(numbers)
    print(average)
