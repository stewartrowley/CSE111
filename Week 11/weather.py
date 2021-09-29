from numpy import minimum
import pandas as pd
pd.set_option('max_row', None)

def main():
    # This program uses pandas to show min or max temprature with wind chill
    # It also will show data of the month of what ever you choose to do.
    # calling the data, to read it in pandas
    read = read_data()
    
    # User inputs the date they want to look up and picks the min or max temprature with a wind chill of the day
    months = input('What month of weather data in Rexburg would you like to see from JANUARY to JULY? ')
    choice = input('What date would you like to pick between 2021-01-01 to 2021-07-04?(yyyy-mm-dd) ')
    wind_chill_choice = input("Which do you want the temprature max with wind chill or temprature min with wind chill of the day?(type - MAX/MIN) ")
     
    # Calls the function for months 
    m = month_data(months, read)
    print(m)

    # # calling functions to get the data
    max_t = get_tempt_max(read, choice)
    min_t = get_tempt_min(read, choice)
    average_wind = average_wind_speed(read, choice)
    
    # # decides whether they chose MIN or MAX and prints the data onto the screen.
    if wind_chill_choice == 'MAX':
        total_max = wind_chill_max(max_t, average_wind)
        print('The max temprature of the day with a wind chill is:')
        print(total_max)

    elif wind_chill_choice =='MIN':
        total_min = wind_chill_max(min_t, average_wind)
        print('The min temprature of the day with a wind chill is:')
        print(total_min)

# This function reads the csv file with pandas 
def read_data():
    df = pd.read_csv('update_rexburg.csv')
    index = df.set_index('DATE')
    return index

# This function takes there date they picked and gets the data from data frame.
def date_choice(decision, option):
    indexed = decision.loc[option]
    return indexed

# This function grabs the days of the month for the data.
def month_data(month, df):
    if month == 'JANUARY':
        month = df.iloc[0:31, [1, 2, 3, 5, 6, 7, 8]]
    elif month == 'FEBUARY':
        month = df.iloc[31:59, [1, 2, 3, 5, 6, 7, ]]
    elif month == 'MARCH':   
        month = df.iloc[59:90, [1, 2, 3, 5, 6, 7, 8]]
    elif month == 'APRIL':
        April = df.iloc[90:120, [1, 2, 3, 5, 6, 7, 8]]
        print(April)
    elif month == 'MAY':
        May = df.iloc[120:151, [1, 2, 3, 5, 6, 7, 8]]
        print(May)
    elif month == 'JUNE':
        June = df.iloc[151:181, [1, 2, 3, 5, 6, 7, 8]]
        print(June)
    elif month == 'JULY':
        July = df.iloc[181:185, [1, 2, 3, 5, 6, 7, 8]]
        print(July)
    return month
    

#  Gets the temprature max from the date they chose in the dataframe.
def get_tempt_max(info, option):
    maximums = info.loc[option, 'TMAX']
    return maximums

# Gets the temprature min from the date they chose in the dataframe.
def get_tempt_min(info, option):
    minimums = info.loc[option, 'TMIN']
    return minimums 

# This function gets the average wind speed.
def average_wind_speed(info, option):
    indexed = info.loc[option, 'AWND']
    return indexed

# This function calculates the max temprature with a wind chill.
def wind_chill_max(tempt_max, wind_speed):
    chill = 35.74 + 0.6215 * tempt_max - 35.75 * (wind_speed ** 0.16) + 0.4275 * tempt_max * (wind_speed ** 0.16)
    return chill

# This function calculates the min temprature with a wind chill.
def wind_chill_min(tempt_low, wind_speed):
    chill = 35.74 + 0.6215 * tempt_low - 35.75 * (wind_speed ** 0.16) + 0.4275 * tempt_low * (wind_speed ** 0.16)
    return chill

if __name__ == "__main__":
    main()
