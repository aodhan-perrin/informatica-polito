def alphToNum(grade: str) -> float:
    match grade[0].upper():
        case 'A':
            num = 4
        case 'B':
            num = 3
        case 'C':
            num = 2
        case 'D':
            num = 1
        case 'F':
            return 0
    
    try:
        match grade[1]:
            case "-":
                return num - 0.3        
            case "+":
                if grade[0] == 'A':
                    return num
                else:
                    return num + 0.3
    except:
        return num

grade = input("input grade -> ")
print(alphToNum(grade))