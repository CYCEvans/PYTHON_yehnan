def getbits(x,p,n):
    return (x>>(p+1-n)&~(~0b0<<n))