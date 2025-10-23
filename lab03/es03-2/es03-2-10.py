from math import sqrt

def escapeV(comet_M: float) -> float:
    return sqrt(2 * ((6.67e-11 * comet_M) / 9.4))


def returnMDiff(comet_M: float, v: float) -> float:
    return ((9.4 * (v+1)**2) / (2 * 6.67e-11)) - comet_M


def returnCheck(comet_M: float, v: float) -> str:
    if v < escapeV(comet_M):
        return f"return possible at mass M"
    else:
        return f"return possible at mass M + {returnMDiff(comet_M, v)}kg"


comet_mass = 2.2e14
v = int(input("velocity -> "))

print(returnCheck(comet_mass, v))

