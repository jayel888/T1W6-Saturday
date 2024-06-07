# Calculator using if-else statements

# Get user input

num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculations using if-else statements

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num1 or num2 != 0:
        result = num1 / num2
    else:
        result = "Undefined"
else:
    result = "Error! Invalid Operation"

print(f"The answer is: {result}")