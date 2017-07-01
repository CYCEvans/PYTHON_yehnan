def divide3(r):
    x = 0
    try:
        for n in str(r):
            x += int(n)
        if x% 3 == 0:
            return True
        else:
            return False
    except:
        return 'Please enter a integer'

if __name__ == '__main__':
    # simple tests
    if divide3(9) != True:
        print('Failed')
    if divide3(37524) != True:
        print('Failed')
    if divide3(21) != True:
        print('Failed')
    if divide3(18) != True:
        print('Failed')
    if divide3(4) != False:
        print('Failed')
