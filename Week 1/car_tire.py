import math

# ask user the dimensions 
print("")
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float (input("Enter the diameter of the wheel in inches (ex 15): "))
model = "GMC Acadia"

# compute the volume
volume = (math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter)) / 10000000
circumference = math.pi * diameter

# display the volume
print("")
print(f"The approximate volume is {volume:.1f} cubic cm.")
print(f"The circumference of the tire would be {circumference:.1f} inches.")
print("")
try_again = input("Would you like to try this again but with different number(YES or NO)? ")
try_again = try_again.lower()

if try_again == "yes":
    while try_again == "yes":
        # ask user the dimensions 
        print("")
        width = float(input("Enter the width of the tire in mm (ex 205): "))
        aspect = float(input("Enter the aspect ratio of the tire (ex 60): "))
        diameter = float (input("Enter the diameter of the wheel in inches (ex 15): "))

        # compute the volume
        volume = (math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter)) / 10000000
        circumference = math.pi * diameter

        # display the volume
        print("")
        print(f"The approximate volume is {volume:.1f} cubic cm.")
        print(f"The circumference of the tire would be {circumference:.1f} inches.")
        print("")

        try_again = input("Would you like to try this again but with different number(YES or NO)? ")
        try_again = try_again.lower()

        if try_again == "no":
            print("")
            print("Have a nice day, good bye!")
elif try_again == "no":
    print("Have a nice day, good bye!")

