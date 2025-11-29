def adjDuplicates(seq: list) -> list:
    dupes = []

    for i in range(len(seq)-1):
        if seq[i] == seq[i+1] and seq[i] not in dupes:
            dupes.append(seq[i])

    return dupes


seq = []

print("insert a sequence of ints (Enter to exit)")
n = input("-> ")

while n != '':
    seq.append(int(n))
    n = input("-> ")

for i in adjDuplicates(seq):
    print(i)
