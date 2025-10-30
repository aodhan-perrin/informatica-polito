a = 32310901
b = 1729
m = 2**24

r = int(input("insert seed -> "))

for _ in range(100):
    r = (a * r + b) % m
    print(r)


