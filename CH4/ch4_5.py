def k(li):
    return li[1]
if __name__ == '__main__':
    data =[('Andre',33,172,66),('Johnnny',25,178,58),('Bob',13,145,38)]
    print(sorted(data))#預設以第一個元素來排列
    print(sorted(data,key=k))#變更以第二個元素排列
    print(sorted(data, key=lambda x: x[2]))#變更以第三個元素排列

