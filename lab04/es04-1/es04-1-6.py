from math import sqrt


def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    else:
        for i in range(2, int(sqrt(n) + 1)):
            if n % i == 0:
                return False
                break
        return True


def infPrimes(n: int) -> list:
    primes = []

    for i in range(n, 0, -1):
        if isPrime(i):
            primes.append(i)

    return primes


n = int(input("insert n -> "))

for prime in infPrimes(n):
    print(prime)
