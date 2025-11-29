from math import sqrt


def primeFactors(n: int) -> list:
    p_factors = []

    while n % 2 == 0:
        p_factors.append(2)
        n //= 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            p_factors.append(i)
            n //= i

    if n > 2:
        print(n)

    return p_factors


n = int(input("insert n -> "))

for factor in primeFactors(n):
    print(factor)
