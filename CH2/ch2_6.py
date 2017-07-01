def gcd(a,b):
    while b:
         a, b = b, a % b
    return a

def lcm(a, b):
    res = (a * b) / gcd(a, b) #最小公倍數為兩者相乘除以最大公因數
    return res

print (lcm(60, 24))


if __name__ == '__main__':
    # simple tests
    if lcm(7, 13) != 91:
        print('Failed')
    if lcm(100, 25) != 100:
        print('Failed')
    if lcm(16, 24) != 48:
        print('Failed')