import math

def findsame(a,b):
    sameList = []
    for x in range(len(a)):
        for y in range(len(b)):
            if a[x] == b[y] :
                sameList.append(a[x])
    return sameList
liA = [1, 5, 3, 4, 6, 7, 10]
liB = [91, 77, 1, 5, 6, 7]

print (findsame(liA, liB))
