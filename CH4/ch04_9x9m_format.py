def p99(li):
    for y in range(1,10):
        result=[]
        for x in li:
            s =" %2d * %2d  = %2d" % (x , y , x*y)
            result.append(s)
        print(' '.join(result))

if __name__ == '__main__':
    lst = [4,5,6]
    print(p99(lst))