from random import getrandbits

x, y = 0, 0

print(f"starting pos: ({x}, {y})")

for i in range(100):
    isX = bool(getrandbits(1))
    isPos = bool(getrandbits(1))

    if isX:
        if isPos:
            x += 1
        else:
            x -= 1
    else:
        if isPos:
            y += 1
        else:
            y -= 1

    print(f"({x}, {y})")
