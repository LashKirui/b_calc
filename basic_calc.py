def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Can't' divide with 0"
    return x / y


operation_dict = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}


def main():
    while True:
        print("Options")
        print("Enter 'add' for addition ")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")

        user_input = input(": ")
        user_input = user_input.lower()

        if user_input == "quit":
            break

        elif user_input in operation_dict:
            num1 = float(input("enter the first number: "))
            num2 = float(input("enter the second number: "))
            operation = operation_dict[user_input]
            result = operation(num1, num2)
            print("result: ", result)
        else:
            print("Invalid input")


main()
