def product(iterable,start=1):
    result = start
    for x in iterable:
        result*=x
    return result
def my_factorial(n):
    return product(range(2,n+1))
print(product([1,2,3,4,5]))
print(my_factorial(6))
