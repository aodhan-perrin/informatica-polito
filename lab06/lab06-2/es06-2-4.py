from math import pi

COPPER_PHI = 1.678e-8
ALU_PHI = 2.82e-8

def diameter(gauge: int) -> float:
    return 0.127 * 92**((36 - gauge) / 39)


def resistance(phi: float, length: float, gauge: int) -> float:
    return (4 * phi * length) / (pi * diameter(gauge)**2)


gauge = int(input("insert wire gauge -> "))
length = int(input("insert wire length (mm) -> "))

print(f"copper resistance: {round(resistance(COPPER_PHI, length, gauge), 2)}")
print(f"aluminum resistance: {round(resistance(ALU_PHI, length, gauge), 2)}")