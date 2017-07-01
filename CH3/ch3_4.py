def collatz(n):
    while n!=1:
        if n%2 ==0 :
            n /= 2
        else:
            n = 3*n+1
    return n
if __name__ == '__main__':
    for i in range(1, 10001):
        if collatz(i) != 1:
            print('collatz_i(' + str(i) + ') failed');
            break
    else:
        print('All passed')