def cumlative_product(iterable,start=1):
    result=[]
    acc= start
    for x in iterable:
        acc *=x
        result.append(acc)
    return result

print(cumlative_product(range(1,11)))