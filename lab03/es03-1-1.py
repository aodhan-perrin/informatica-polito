from math import sqrt

def isEqual(a, b) -> bool:
    return a == b

print(isEqual(1, 1))
print(isEqual(1, 1.0))
print(isEqual(2.0, sqrt(4)))
print(isEqual('1', 1))
print(isEqual('ciao', 'Ciao'))
