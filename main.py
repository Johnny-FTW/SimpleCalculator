import tools


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return round(x / y, 2)



def main():
    while True:
        print("##################")
        print("CALCULATOR APP")
        print("##################")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. QUIT APP")
        print("6. Add from file")
        print("##################")

        choice = input("Enter choice:")
        print(choice)

        if choice in ("1", "2", "3", "4", "5", "6"):
            if choice == "6":
                nums = tools.load_nums_from_file()
                for pair in nums:
                    x = pair[0]
                    y = pair[1]
                    print(f"{x}+{y} = {add(x, y)}")
            elif choice == "5":
                print("Good bye")
                break
            else:
                x = int(input("Insert first number:"))
                y = int(input("Insert second number:"))
                if choice == "1":
                    print(f"{x} + {y} is {add(x, y)}")
                elif choice == "2":
                    print(f"{x} - {y} is {subtract(x, y)}")
                elif choice == "3":
                    print(f"{x} * {y} is {multiply(x, y)}")
                elif choice == "4":
                    print(f"{x} / {y} is {divide(x, y)}")
        else:
            print("Invalid input")


if __name__ == "__main__":              #uz ide aj testovanie
    main()