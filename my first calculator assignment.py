#  my Simple Calculator for Whole Numbers

# Step 1: Get numbers into the program
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Step 2: Get the operation to perform
operation = input("Enter the operation (+, -, *, /): ")

# Step 3 & 4: Calculate and display result 
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Invalid operation!")
    exit()

print(f"{num1} {operation} {num2} = {result}")
