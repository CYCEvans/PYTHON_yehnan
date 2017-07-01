def my_sum(iterable,start=0):
    result=start
    for x in iterable:
        result +=x
    return result

print(my_sum([1,8,9,15]))
print(my_sum(["xdsas","zz","scsa"],"")) # 支援字串list，起始值要改