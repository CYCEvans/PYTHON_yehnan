def ozen(n):
    nabc = n
    ncba = int(str(nabc)[::-1]) #先將abc字母反轉後，改成int型式
    ndef = abs(nabc - ncba) # 相減得出絕對值
    nfed = int(str(ndef)[::-1])# 將def字母反轉後，改成int型式
    return (ndef + nfed) == 1089 #回傳bool
if __name__ == '__main__':
    # simple test
    if ozen(732) != True:
        print('Failed')
    if ozen(654) != True:
        print('Failed')
    if ozen(123) != True:
        print('Failed')
    for x in range(1, 9 + 1): # 百位
        for y in range(0, 9 + 1): # 十位
            for z in range(0, 9 + 1): # 個位
                n = x * 100 + y * 10 + z
                if ozen(n) != (abs(x - z) >= 2):
                    print('Failed: %d' % n);