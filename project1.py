# The Addition operation

def add(a, b):
    return a + b
# The Subtraction Operation


def subtract(a, b):
    return a - b
# The Multiplication operation


def multiply(a, b):
    return a * b
# The Division Operation


def divide(a, b):
    return a / b


# The Operational processes
print("Select Your Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

# The main process that performs the operation you select

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options, the you proceed
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
