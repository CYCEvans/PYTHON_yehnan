def prime(n):
    for i in range(2, n):
        if n % i == 0: # 在本身到2的範圍中找數看看有沒有能整除自己的
            return False
    return True
if __name__ == '__main__':
    # simple tests
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    not_primes = [4, 6, 15, 20, 21, 25, 100, 246]
    for i in primes:
        if prime(i) != True:
            print('Failed: %d is prime' % i)
    for i in not_primes:
        if prime(i) != True:
            print('Failed: %d is not prime' % i)