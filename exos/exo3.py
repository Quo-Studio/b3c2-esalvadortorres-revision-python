number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

result = number1 + number2
difference = number1 - number2
product = number1 * number2

if number2 != 0:
    division = number1 / number2
else:
    division = "Division by zero is not possible."

print(f"Sum: {result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Division: {division}")
