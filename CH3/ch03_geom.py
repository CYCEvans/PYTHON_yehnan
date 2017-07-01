def geomean(n):
    p = 1
    for x in n:
        p *= x
    return p ** (1.0/len(n))
