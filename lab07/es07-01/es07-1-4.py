def localmax(an: list) -> list[int]:
    maximums = []

    for i in range(1, len(an)-1):
        if an[i] > an[i-1] and an[i] > an[i+1]:
            maximums.append(an[i])

    return maximums



an = []
n = input("insert whole numbers (Enter to quit):\n-> ")

while n != '':
    try:
        an.append(int(n))
    except:
        print("error: invalid input")

    n = input("-> ")

if localmax(an) == []:
    print("there are no local maximums")
else:
    for n in localmax(an):
        print(n, end=' ')
