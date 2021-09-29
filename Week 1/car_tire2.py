import math

# ask user the dimensions
tire_numbers = ""
tire_numbers = tire_numbers.lower()
while tire_numbers != "no":
    tire_numbers = input("Would you like to see what the volume is for your tire(yes/no)?  ")
    if tire_numbers == "yes":

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

        
        # from datetime import datetime
        # shortDate = datetime.today().strftime("%Y-%m-%d")

        from datetime import date
        import random

        start_date = date.today().replace(day=1, month=1).toordinal()
        end_date = date.today().toordinal()
        random_day = date.fromordinal(random.randint(start_date, end_date))

        with open("volumes.txt", mode="at") as volum_file:
            print(f"{random_day}, {width}, {aspect}, {diameter}, {volume:.1f}", file=volum_file)

    elif tire_numbers == "no":
        buy_tire = input("Would you like to buy the tire with those dimensions(yes/no)? ")
        buy_tire = buy_tire.lower()
        
        if buy_tire == "yes":
            phone_number = input("What is your phone number? ")
            print("We will take care of this soon and get the tire ordered for you.")
                
            with open("volumes.txt", mode="at") as volum_file:
                print(f"{phone_number}", file=volum_file)
                
            print("Thank you for your business!")
        
        elif buy_tire == "no":
            print("Thank you for your time! Have a good day!")


    
