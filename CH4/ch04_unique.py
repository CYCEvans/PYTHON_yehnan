# 出現過的元素
def unique(iterable):
    result=[]
    for x in iterable:
        if x not in result:
            result.append(x)
    return result

if __name__ == '__main__':
    lst = [4,8,9,5,7,2,1,7,4,9,8,5]
    print(unique(lst))