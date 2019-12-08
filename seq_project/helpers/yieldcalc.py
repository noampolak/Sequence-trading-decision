def retval(yieldArray, startIndex, endIndex):
    s = 1
    for i in range(startIndex, endIndex):
        s *= (1+yieldArray(i))
    return s - 1

