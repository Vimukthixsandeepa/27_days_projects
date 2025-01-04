#function to add two numbers
def add(x, y):
    return x + y
#function to subtract two numbers
def subtract(x, y):
    return x - y
#function to multiply two numbers
def multiply(x, y):
    return x * y
#function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
#function to calculate power of a number
def power(x, y):
    return x ** y
#function to calculate square root of a number 
def sqrt(x):
    return x ** 0.5
def calculator():
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Square root")
    choice = input("Enter choice(1/2/3/4/5/6): ")
    num1 = float(input("Enter first number: "))
    if choice != '6':
        num2 = float(input("Enter second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print(num1, "^", num2, "=", power(num1, num2))
    elif choice == '6':
        print("Square root of", num1, "=", sqrt(num1))
    else:
        print("Invalid input")
calculator()