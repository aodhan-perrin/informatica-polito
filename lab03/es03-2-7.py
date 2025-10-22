def magnitude(prefix: str) -> float:
    match prefix:
        case 'k':
            return 10e3
        case 'c':
            return 10e-2
        case 'm':
            return 10e-3
        case _:
            return 1


def convert(start: str, end: str, value: float) -> float:
    return value * (magnitude(start[0]) / magnitude(end[0]))


def conversionCheck(input: str, units: list) -> list:
    compatible_units = []

    for unit in units:
        if unit[-1] == input[-1] and unit != input:
            compatible_units.append(unit)

    return compatible_units


units = ["ml", "l", "g", "kg", "mm", "cm", "km"]

while True:
    start_unit = input(f"convert from {units} -> ")

    if start_unit in units:
        compatible_units = conversionCheck(start_unit, units)
        
        while True:
            end_unit = input(f"convert to {compatible_units} -> ")

            if end_unit in compatible_units:
                value = float(input(f"value of {start_unit} to convert -> "))
                print(f"{convert(start_unit, end_unit, value)}{end_unit}")
                
                break
            else:
                print("error: incompatible conversion\n")
        break
    else:
        print("error: unsupported type\n")
