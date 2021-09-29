def main():
    start = float(input("What is your starting odometer value in miles? "))
    end = float(input("What is your ending odometer value in miles? "))
    fuel_amount = float(input("What is the amount of fuel in gallons you have? "))
    
    mpg = miles_per_gallon(start, end, fuel_amount)
    lp100k = lp100k_from_mpg(mpg)

    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")
    pass

def miles_per_gallon(start, end, fuel_amount):
    mpg = (end - start) / fuel_amount
    return mpg 

def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg 
    return lp100k

main()
