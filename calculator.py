def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

def validate_option():
    while True:
        try:
            option = int(input("Enter option for operation: "))
            if 1 <= option <= 5:
                return option
            else:
                print("Please enter a valid option between 1 - 5.")
        except ValueError:
            print("Please enter a valid numeric option")


def validate_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print(f"ValueError:{e}")

def main():
    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        option = validate_option()

        if option == 5:
            print("You chose to exit! Good Bye")
            exit()

        num1 = validate_input("Enter first number: ")
        if option == 4:
            while True:
                num2 = validate_input("Enter second number: ")
                if num2 == 0:
                    print("Cannot divide by zero.Please enter non-zero number")
                else:
                    break
        else:
            num2 = validate_input("Enter second number: ")


        if option == 1:
            result = add(num1, num2)
            print(f"Addition: {num1} + {num2} = {result}")
        elif option == 2:
            result = subtract(num1, num2)
            print(f"Subtraction: {num1} - {num2} = {result}")
        elif option == 3:
            result = multiply(num1, num2)
            print(f"Multiplication: {num1} * {num2} = {result}")
        elif option == 4:
            try:
                result = divide(num1, num2)
                print(f"Division: {num1} / {num2} = {result}")
            except ValueError as e:
                print(f"ValueError: {e}")

        choice = input("Do you want to continue? [y/n]")
        if choice == "y":
            continue
        else:
            exit()


if __name__ =="__main__":
    main()