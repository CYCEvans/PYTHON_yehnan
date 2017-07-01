pi = 3.14
#求最大功因數
def gcd(a,b):
    while b:
        a,b = b, a%b # 最大公因數為 b代入a ， b 由 a%b 代入，作迴圈直到 b == a ，a 即是最大功因式
    return a
#n階
def fractional(n):
    result = 1
    for i in range(1,n+1): #1~n
        result *= i
    return result
if __name__ == '__main__':
    print('as main program')
else:
    print('as module')