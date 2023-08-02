menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

try:
    while True:
        order = input("Item: ").title()
        for food, price in menu.items():
            if order == food:
                total += price
                print(f"Total: ${total:.2f}")
                break

except (EOFError, KeyError):
    pass