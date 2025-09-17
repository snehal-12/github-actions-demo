def validate_input():
    try:
        float(input("Enter a number: "))
        return True
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a valid option.")
        continue

    if option == 5:
        print("You chose to exit! Good Bye")
        exit()
    elif option not in range (1,5):
        print("Please enter a valid option between 1 - 5.")
        continue

    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))

    if option == 1:
        result = num1 + num2
        print(f"Addition: {num1} + {num2} = {result}")
    elif option == 2:
        result = num1 - num2
        print(f"Subtraction: {num1} - {num2} = {result}")
    elif option == 3:
        result = num1 * num2
        print(f"Multiplication: {num1} * {num2} = {result}")
    elif option == 4:
        if num2 == 0:
            print("Error: Can't divide by zero")
        else:
            result = num1 / num2
            print(f"Division: {num1} / {num2} = {result}")
            
    choice = input("Do you want to continue? [y/n]")
    if choice == "y":
        continue
    else:
        exit()