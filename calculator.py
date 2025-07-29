action = input("Enter action (add, sub, mul, div): ").strip().lower()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if action == "add":
    result = num1 + num2
elif action == "sub":
    result = num1 - num2
elif action == "mul":
    result = num1 * num2
elif action == "div":
    if num2 == 0:
        result = "Cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid action"
print("Result:", result)