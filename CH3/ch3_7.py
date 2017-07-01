import math
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def stirling(n):
    pi = math.pi
    return(math.sqrt(2*pi*n)*math.pow(n/math.exp(1),n))
if __name__ == '__main__':
    # simple test
    for n in range(2, 21):
        nf = factorial(n)
        nfs = stirling(n)
        print('%d! = %d, stirling: %f' % (n, nf, nfs))
        print('error: %f percent' % ((nfs - nf) / nf*100))
