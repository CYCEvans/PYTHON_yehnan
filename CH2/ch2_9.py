import math

def sumFacDigits(n):
    nFac = math.factorial(n)
    sum = 0
    for x in str(nFac):
        sum += int(x)
    print(nFac,sum)
    
sumFacDigits(9)
sumFacDigits(5)
