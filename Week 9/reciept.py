# Example 2

import csv 


def main():
    # Indexes of some of the columns
    KEY_INDEX = 0
    FOOD_INDEX = 1
    PRICE_INDEX = 2

   
    reciept = read_products("products.csv", KEY_INDEX, FOOD_INDEX, PRICE_INDEX)
    request = process_request("request.csv", KEY_INDEX, FOOD_INDEX)
    
    # products[KEY_INDEX] = FOOD_INDEX[1], PRICE_INDEX[2]
    # Print the reciept dictionary.
    print("Products:")
    for i in reciept:
       
        items = reciept[i]
        key = items[0]
        food = items[1]
        price = items[2]
        print(f"{key} [{food}, {price}]")
        
    for line in request:
        item_type = request[line]
        key_value = item_type[0]
        key_type = key[key_value]
        food_type = key_type[0]
        print(food_type)

        
        
        # print(f"{key_item}: {quantity} @ {price}")
        
       
    


def read_products(filename, key_column_index, food_column_index, price_column_index):
    # Create an empty dictionary that will
    # store the data from the CSV file.
    filename = "products.csv"
    product_dictionary = {}

    # Open a CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:
            # From the current row, retrieve
            # the column that contains the key.
            key = row[key_column_index]
            food = row[food_column_index]
            price = row[price_column_index]
            
            # Store the data from the current row
            # into the dictionary.
            product_dictionary[f"{key} ['{food}', '{price}']"] = row

    return product_dictionary

def process_request(filename, key_column_index, quantity_column_index):
    
    filename = "request.csv"
    request_dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row in reader:
            
            key = row[key_column_index]
            quantity = row[quantity_column_index]
            
            request_dictionary[f"{key}: {quantity}"] = row

        
    
        

    return request_dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()