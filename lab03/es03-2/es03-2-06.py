def tax(income: float, isMarried: bool) -> float:
    if isMarried:
        if income > 0 and income <= 16000:
            return income * 0.10
        elif income > 16000 and income <= 64000:
            return 1600 + (income * 0.15)
        elif income > 64000:
            return 8800 + (income * 0.25)
        else:
            return 0.0
    else:
        if income > 0 and income <= 8000:
            return income * 0.10
        elif income > 8000 and income <= 32000:
            return 800 + (income * 0.15)
        elif income > 32000:
            return 4400 + (income * 0.25)
        else:
            return 0.0


while True:
    isMarried = input("are you married? [y/n] -> ")

    match isMarried:
        case 'y':
            isMarried = True
            break
        case 'n':
            isMarried = False
            break
        case _:
            print("error: invalid input")


income = float(input("insert income (€) -> "))

print(f"your amount due is: €{tax(income, isMarried)}")