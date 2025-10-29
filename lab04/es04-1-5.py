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


n = int(input("insert n -> "))
print(f"{n} is prime: {isPrime(n)}")
