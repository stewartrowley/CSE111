import random

def append_random_numbers(quanitiy, numbers_list[]):
    number = random.uniform(quanitiy(1, 100))
    rounded = round(number, 1)
    numbers_list.append(rounded)
    return numbers_list

def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)
    