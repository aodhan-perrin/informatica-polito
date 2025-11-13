from random import randint

def evensplit(randoms: list) -> dict:
    split = {
        "evens": [],
        "odds": [],
    }

    for n in randoms:
        if n % 2 == 0:
            split["evens"].append(n)
        else:
            split["odds"].append(n)
        
    return split


def randlist() -> list[int]:
    randoms = []
    
    for i in range(10):
        randoms.append(randint(0, 100))

    return randoms


randoms = randlist()
split = evensplit(randoms)

for i in split["evens"]:
    print(i, end=' ')
print()

for i in split["odds"]:
    print(i, end=' ')
print()

for i in randoms[::-1]:
    print(i, end=' ')
print()

print(randoms[0], randoms[-1])