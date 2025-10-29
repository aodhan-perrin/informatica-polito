def subs(string: str) -> list:
    n = len(string)
    substrings = []

    for start in range(n):
        for end in range(start+1, n+1):
            substrings.append(string[start:end])

    return substrings


string = input("insert string -> ")
substrings = sorted(subs(string), key=len)

for string in substrings:
    print(string)
