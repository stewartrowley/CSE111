# """
# When you physically exercise to strengthen your heart, you
# should maintain your heart rate within a range for at least 20
# minutes. To find that range, subtract your age from 220. This
# difference is your maximum heart rate per minute. Your heart
# simply will not beat faster than this maximum (220 - age).
# When exercising to strengthen your heart, you should keep your
# heart rate between 65% and 85% of your heart's maximum.
# """

# asking user for age
age = int(input("Please enter your age: "))

# computing heart rate
max_heart = (220 - age)
high_exercise = int((.85 * max_heart))
low_exercise = int((.65 * max_heart))

# displaying results

print(f"When you exercise to strengthen your heart, you should\nkeep your heart rate between {low_exercise} and {high_exercise} beats per minute. ")

