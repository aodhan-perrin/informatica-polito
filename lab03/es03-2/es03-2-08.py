def bonus(expense: float) -> float:
    if expense < 10:
        return 0
    elif expense >= 10 and expense < 60:
        return expense * 0.08
    elif expense >= 60 and expense < 150:
        return expense * 0.1
    elif expense >= 150 and expense < 210:
        return expense * 0.12
    else:
        return expense * 0.14


expense = float(input("money spent -> "))
print(f"you got a {round(bonus(expense), 2)} bonus!")
