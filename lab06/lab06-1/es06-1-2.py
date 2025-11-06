def count_words(string: str) -> int:
    count = 1

    for index in range(len(string)):
        if string[index] == ' ' and string [index - 1 ] != ' ':
            count += 1

    return count


print(count_words("this  is    a string"))