def calculate(expression):
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        if z == 0:
            print("Error: Division by zero is not allowed.")
            return None
        result = x / z

    return round(float(result), 1)

user_input = input("Enter an arithmetic expression: ")
result = calculate(user_input)
if result is not None:
    print(result)
    


