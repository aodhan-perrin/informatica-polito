VOWELS = "aeiou"

def count_vowels(string: str) -> int:
    count = 0

    for char in string:
        if char.lower() in VOWELS:
            count += 1
            
    return count