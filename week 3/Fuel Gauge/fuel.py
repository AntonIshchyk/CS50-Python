while True:
    try:
        fraction = input("Fraction: ")
        numerator, denominator = map(int, fraction.split("/"))
        percentageNumber = round((numerator / denominator) * 100)

        if numerator > denominator:
            continue

        if percentageNumber <= 1:
            print("E")
            break
        elif percentageNumber >= 99:
            print("F")
            break
        else:
            print(percentageNumber, "%" , sep = "")
            break
    except (ValueError, ZeroDivisionError):
        pass