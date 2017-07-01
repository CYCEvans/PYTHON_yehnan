alphabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def base36encode(number , alphabet = alphabet):
    result = []
    base = len(alphabet)
    sign=''
    if number <0:#如果輸入的是負數
        sign = '-'
        number = -number#先轉成正數
    while number >= base:#如果大於36
        number, i = divmod(number, base)#不斷除36，得到商和餘數
        result.append(alphabet[i]) # 找出餘數相對應的字元加入list
    result.append(alphabet[number])

    if sign =='-':
        result.append(sign) #如果是負數須加上-

    return ''.join(reversed(result)) #反過來之後冠連起來

if __name__ == "__main__":
    print(base36encode(1678244))
