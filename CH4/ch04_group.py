# 切割串列，根據指定的長度切成好幾塊
def group(iterable,size):
    result = []
    li = list(iterable)#將可迭代者轉成list
    length=len(li)
    for i in range(0,length,size):#一你要的長度開始迭帶到最大長度
        result.append(li[i:i+size])#加入可迭代者串列的長度個數，如果最後小於所需長度，全部加入
    return result

if __name__ == '__main__':
    lst = [4,8,9,5,7,2,1,7,4,9]
    print(group(lst,4))
    tup = (4,8,9,5,7,2,1,7,4,9)
    print(group(tup,4))
