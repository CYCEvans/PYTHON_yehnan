def a(li):
    count = 0
    result=[]
    # for i in range(len(li)):
    #     li[i] = li[i]+count
    #     count +=1
    for i, e in enumerate(li):
        result.append(e + i)
    return result
    # return li

if __name__ == "__main__":
    li = [8, 4, 1, 7]
    if a(li) != [8, 5, 3, 10]:
        print('Failed')
    li = [10, 11, 12, 13]
    if a(li) != [10, 12, 14, 16]:
        print('Failed')
    li = [4,7,8,4,9,8,7]
    print(a(li))
