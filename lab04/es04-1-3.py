n = int(input("insert side length -> "))

for i in range(0, n):
    print('*' * n)

print()

for i in range(n):
    print(" "*(n - i), "*"*(i*2 + 1))
for i in range(n-2, -1, -1):
    print(" "*(n - i), "*"*(i*2 + 1))
