def cumlative_sum(iterable,start=0):
    result=[]
    acc= start
    for x in iterable:
        acc +=x
        result.append(acc)
    return result

print(cumlative_sum(range(1,11)))