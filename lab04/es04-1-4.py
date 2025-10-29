string = input("input string -> ")

print(f"reversed: {string[::-1]}")

revCaps = ''

for char in string:
    if char.isupper():
        revCaps += char

print(f"reversed uppercase: {revCaps[::-1]}")
