import pandas as pd
pd.set_option('max_row', None)

def main():
    weather = pd.read_csv('seaside_oregon.csv')
    # print(weather)

    # DataFrame organizes the table
    df = pd.DataFrame(weather)
    # print(df)

    # prints a specific column
    # column = df['DATE']
    # column = df.DATE
    # dated = column['2021-05-23']
    # print(dated)

    # prints multiple columns 
    # mult_column = df[['DATE', 'NAME']]
    # print(mult_column)

    # print by iloc
    # row = df.iloc[0]
    # print(row)

    # prints multiple row
    mult_row = df.iloc[[0, 2], 1:4]
    print(mult_row)
    
    # prints number of rows and columns 
    # print(df.shape)

    # counts the amount of time the value is in there
    # print(df['NAME'].value_counts())
    
    # gets multiple and specific
    # print(df.loc[1:3, 'NAME':'SNOW'])
  



    # # shape - tuple (number of rows, number of columns)
    # shaped = weather.shape
    # print(shaped)

    # # info - print a concise summary of a DataFrame
    # info_data = weather.info
    # print(info_data)

    # # head first values 
    # head_num = weather.head(10)
    # print(head_num)

    # # tails last values
    # tails_num = weather.tail(10)
    # print(tails_num)


if __name__ == "__main__":
    main()