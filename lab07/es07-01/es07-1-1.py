def alt_sum(seq: list[int]) -> int:
    sum = 0

    for i in range(len(seq)):
        if i % 2 == 0:
            sum += seq[i]
        else:
            sum -= seq[i]

    return sum


seq = []
n = input("insert whole numbers (Enter to quit):\n-> ")

while n != '':
    try:
        seq.append(int(n))
    except:
        print("error: invalid input")

    n = input("-> ")

print(alt_sum(seq))