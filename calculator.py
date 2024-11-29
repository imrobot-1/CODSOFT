def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: Division by zero ") 
    else:
        return x / y

print("Welcome to Calculator")
print("Select an operation:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n0. Quit")

while True:
    choice = input("Enter choice (1/2/3/4/0): ")

    if choice == '0':
        print("Thank you for using Calculator")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4/0).")

