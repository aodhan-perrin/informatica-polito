string = "I am DEFINITELY an int == 28"

vowels = 'aeiou'
digitCount = 0
uppercase, evenIndex, vowelIndexes, underscoreStr = '', '', '', ''

for index in range(0, len(string)):
    char = string[index]

    # I.
    if char.isupper():
        uppercase += char

    # II.
    if index % 2 == 0:
        evenIndex += char

    # III.
    if char in vowels:
        underscoreStr += '_'
    else:
        underscoreStr += char

    # VI.
    if char.isdigit():
        digitCount += 1

    # V.
    if char.lower() in vowels:
        vowelIndexes += str(index) + ", "

print(
    f"uppercase letters:   {uppercase}\n"
    f"even indexes:        {evenIndex}\n"
    f"with underscores:    {underscoreStr}\n"
    f"no. of digits:       {digitCount}\n"
    f"indexes with vowels: {vowelIndexes}\n"
)
