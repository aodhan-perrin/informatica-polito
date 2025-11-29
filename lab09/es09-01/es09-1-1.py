def swapExtremes(nlist: list[int]) -> list[int]:
    buf = nlist[0]
    nlist[0] = nlist[-1]
    nlist[-1] = buf

    return nlist


def moveElements(nlist: list[int]) -> list[int]:
    buf = nlist.pop()
    nlist.insert(0, buf)

    return nlist


def evenZeros(nlist: list[int]) -> list[int]:
    for i in range(len(nlist)):
        if nlist[i] % 2 == 0:
            nlist[i] = 0

    return nlist


def majLimit(nlist: list[int]) -> list[int]:
    for i in range(1, len(nlist)-1):
        if nlist[i-1] > nlist[i+1]:
            nlist[i] = nlist[i-1]
        elif nlist[i-1] < nlist[i+1]:
            nlist[i] = nlist[i+1]

    return nlist


def rmMiddle(nlist: list[int]) -> list[int]:
    if len(nlist) % 2 != 0:
        middle = int(((len(nlist)-1) / 2))
        nlist.pop(middle)
    else:
        middle = int(len(nlist) / 2)
        nlist.pop(middle)
        nlist.pop(middle-1)

    return nlist


def sortEvens(nlist: list[int]) -> list[int]:
    count = 0
    
    for i in range(len(nlist)):
        if nlist[i] % 2 == 0:
            buf = nlist.pop(i)
            nlist.insert(count, buf)
            count += 1

    return nlist


def secondMax(nlist: list[int]) -> int:
    nlist.remove(max(nlist))
    return max(nlist)




nlist = [0, 1, 3, 4, 5, 6]

#print(swapExtremes(nlist))
#print(moveElements(nlist))
#print(evenZeros(nlist))
#print(majLimit(nlist))
#print(rmMiddle(nlist))
#print(sortEvens(nlist))
print(secondMax(nlist))
