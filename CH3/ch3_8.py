import math
def cardano(a,b,c):
    if 8*(a**3) + 15*(a**2) + 6*a -27*c*(b**2)== 1:
        return True
if __name__ == '__main__':
    # simple test
    count = 0
    for a in range(1, 999):#1~998
        for b in range(1, 1000-a):#1~(1000-a)-1
            for c in range(1, 1000-a-b + 1):#1~(1000-a-b)
                if cardano(a, b, c):
                    count +=1
                    # print(a, b, c)

    print(count)
