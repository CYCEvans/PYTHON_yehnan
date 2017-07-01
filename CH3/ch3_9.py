def checkab(n,m):
    counta = 0
    countb = 0
    for i in range(0,len(n)):
        if n[i]==m[i] :
            counta +=1
        elif n[i] in m:
            countb +=1
    return(counta,countb)
if __name__ == '__main__':
    # simple test
    if checkab('5234', '5346') != (1, 2):
        # print(checkab('5234', '5346'))
        print('Failed: answer 5234, guess 5346')
    if checkab('5234', '5234') != (4, 0):
        # print(checkab('5234', '5234'))
        print('Failed: answer 5234, guess 5234')
    if checkab('1234', '4321') != (0, 4):
        print('Failed: answer 1234, guess 4321')
    if checkab('1234', '2134') != (2, 2):
        print('Failed: answer 1234, guess 2134')
    if checkab('1234', '3241') != (1, 3):
        print('Failed: answer 1234, guess 3241')
