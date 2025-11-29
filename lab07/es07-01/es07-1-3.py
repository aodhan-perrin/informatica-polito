def remove_min(v: list) -> int:
    min = v[0]
    min_index = 0
    
    for i in range(len(v)):
        if v[i] < min:
            min = v[i]
            min_index = i
    

    return(v.pop(min_index))
