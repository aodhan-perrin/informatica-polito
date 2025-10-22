def isLeap(year: int) -> bool:
    '''
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else: return True
    else:
        return False
    '''
    
    # the if statement is equivalent to this single boolean statement:
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))    


# while loop to check if the user inputs a year under 1582
# if not, prompt again

while True:
    year = int(input("insert year over 1582 -> "))
    
    if year > 1582:
        print(isLeap(year))
        break
    else:
        print("_over 1582_\n")
