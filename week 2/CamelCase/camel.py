user_input = input("camelCase: ")
print("snake_case: ", end = "" )
for l in user_input:
    if l.isupper():
        print("_" + l.lower(),end = "")
    else:
        print(l, end = "")
print()