def symbol(numeral_symbol: str) -> int:
    match numeral_symbol.upper():
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L':
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000


def num_to_int(numeral: str) -> int:
    result = 0

    for i in range(len(numeral)):
        if i > 0 and symbol(numeral[i]) > symbol(numeral[i-1]):
            result += symbol(numeral[i]) - 2 * symbol(numeral[i-1])
        else:
            result += symbol(numeral[i])

    return result


numeral = input("insert numeral -> ")
print(num_to_int(numeral))
