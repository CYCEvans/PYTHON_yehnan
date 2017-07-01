def max2sqr(x,y,z):
    n = [x,y,z]
    a = max(n)
    n.remove(a)
    b = max(n)
    return a**2+b**2
print(max2sqr(2,3,4))

if __name__ == '__main__':
    # simple tests
    if max2sqr(1, 2, 3) != 13:
        print('Failed')
    if max2sqr(5, 3, 4) != 41:
        print('Failed')
    if max2sqr(9, 11, 10) != 221:
        print('Failed')