def sum_without_smallest(v: list) -> float:
    sum = 0

    for n in v:
        if n != min(v):
            sum += n

    return sum
        

v = [2, 3, 2, 8, 1, 4]
print(sum_without_smallest(v))
