from random import randint

seq = []


for _ in range(20):
    seq.append(randint(0, 99))

print(seq)

seq.sort()

print(seq)
