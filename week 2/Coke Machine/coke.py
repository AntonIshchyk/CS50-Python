price = 50
coins = [25, 10, 5]

while price != 0:
    user_input = int(input("Insert Coin: "))
    if user_input not in coins:
        print("Amount Due: 50")

    price = price - user_input
    if price <= 0:
        change = abs(price)
        print("Change Owed:", change)
        price = 0
    else:
        print("Amount Due:", price)
    
