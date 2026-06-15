def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b  # Added this line to fix a small bug so division actually returns the result!


while True:
    print("\n--- Welcome to the Python Calculator ---")
    print("This program accepts two numbers and an operator to perform calculations.")
    
    # Using float instead of int allows the user to calculate decimals (e.g., 2.5 + 3.1)
    num1 = float(input("Enter the first number: "))

    operator = input("Choose an operator (+, -, *, /) or type 'exit' to quit: ")

    if operator.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
        
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        result = plus(num1, num2)
        print(f"Result: {result}")
    elif operator == '-':
        result = minus(num1, num2)
        print(f"Result: {result}")
    elif operator == '*':
        result = multiply(num1, num2)
        print(f"Result: {result}") 
    elif operator == '/':
        result = divide(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid operator! Please select a correct operator.")
