print("Welcome to the number sequence generator!")
x = int(input("Enter the start number (x): "))
y = int(input("Enter the end number (y): "))

choice = ""

if choice != "4":
    print("1. Show me the even numbers from x to y")
    print("2. Show me the odd numbers from x to y")
    print("3. Show me the squares of the numbers from x to y")
    print("4. Exit the program")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Even numbers between", x, "and", y)
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end="")
        print("\n") #new line code

    elif choice == "2":
        print("odd numbers between x and y")
        for i in range(x, y + 1):
            if i % 2 != 0:
                print(i, end="")
        print("\n") #new ine code

    elif choice == "3":
        print("Squares of numbers between", x, "and", y)
        for i in range(x, y + 1):
            print(i ** 2, end="")
        print() #new line code

    elif choice == "4":
        print("Close.")

    else:
        print("Invalid choice.")

print("Program Terminated.")
