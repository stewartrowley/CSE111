def main():
    try:
    # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")  

        reversed_fruit = fruit_list.reverse()
        print(f"reversed: {reversed_fruit}")
    
        fruit_list.append("orange")
        print("append orange: {fruit_list}")

        pos = fruit_list.index("apple")
        fruit_list.insert(pos, "cherry")
        print(f"insert cherry: {fruit_list}")

        fruit_list.remove("banana")
        print(f"remove banana {fruit_list}")

        fruit_list.pop()
        print(fruit_list)

        fruit_list.sort()
        print(fruit_list)

        fruit_list.clear()
        print(f"cleared: {fruit_list}")

    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")


if __name__ == "__main__":
    main()