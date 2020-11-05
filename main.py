
num1 = float(input("Enter a number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter a second number: "))
# Inputs created for 2 numbers and an operator with text prompts

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
# If statement for all the operators and else statement for errors
