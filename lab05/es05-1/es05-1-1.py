PIN = 1234

tries = 3

while tries > 0:
    userInput = int(input("\ninsert PIN -> "))

    if userInput == PIN:
        print("PIN correct")
        break
    else:
        print("PIN incorrect")
        tries -= 1

if tries == 0:
    print("\ncard blocked")

