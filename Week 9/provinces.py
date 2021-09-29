def main():
    provinces  =  read_list("provinces.txt")
    # text_list.pop([0])
    # text_list.remove(text_list[0])
     
    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"
    #print(provinces)

    # Call the list.count method which will count the
    # number of times that Alberta appears in the list.
    count = provinces.count("Alberta")

    print(provinces)
    print()
    print(f"Alberta occurs {count} times in the modified list.") 


def read_list(filename):
    text_list = []

    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list

if __name__ == "__main__":
    main()    
