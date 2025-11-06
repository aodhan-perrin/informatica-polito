def saldo(anni: int, saldo_iniziale: int, tasso: float) -> float:
    return saldo_iniziale + (anni * (saldo_iniziale * tasso))


anni = int(input("inserisci anni -> "))
saldo_iniziale = int(input("inserisci il saldo iniziale -> "))
tasso = float(input("inserisci tasso -> "))

print(saldo(anni, saldo_iniziale, tasso))