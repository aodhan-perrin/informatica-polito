def numToAlph(grade: float) -> str:
    if grade == 4.0:
        return "A+"
    elif grade >= 3.85 and grade < 4.0:
        return "A"
    elif grade >= 3.5 and grade < 3.85:
        return "A-"
    elif grade >= 3.15 and grade < 3.5:
        return "B+"
    elif grade >= 2.85 and grade < 3.15:
        return "B"
    elif grade >= 2.5 and grade < 2.85:
        return "B-"
    elif grade >= 2.15 and grade < 2.5:
        return "C+"
    elif grade >= 1.85 and grade < 2.15:
        return "C"
    elif grade >= 1.5 and grade < 1.85:
        return "C-"
    elif grade >= 1.15 and grade < 1.5:
        return "D+"
    elif grade >= 0.85 and grade < 1.15:
        return "D"
    elif grade >= 0.5 and grade < 0.85:
        return "D-"
    elif grade < 0.5:
        return "F"
    else:
        return f"sure... real believable {grade}"


grade = float(input("input grade -> "))
print(numToAlph(grade))