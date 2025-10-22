def order(a, b, c) -> str:
    if a < b < c:
        return "increasing"
    elif a > b > c:
        return "decreasing"
    else:
        return "neither"
    
print(order(1, 2, 3))