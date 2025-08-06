def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def calculator():
    print("Basic CLI Calculator")
    print("Available operations: +, -, *, **, /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, **, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '**':
                result = power(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                raise ValueError("Invalid operation")

            print(f"Result: {result}\n")

        except ValueError as ve:
            print(f"Input Error: {ve}\n")
        except ZeroDivisionError as zde:
            print(f"Math Error: {zde}\n")
        except Exception as e:
            print(f"Unexpected Error: {e}\n")

        again = input("Do you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Exiting calculator. Goodbye!")
            break

# Run the calculator
calculator()










































