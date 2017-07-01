def k(x):
    return len(x)#根據長度來排列
def k1(x):
    return x[1]#根據第二個元素來排
def k3(x):
    return len(x[0])#根據長度來排列

if __name__ == '__main__':
    li=['python','perl','java','c','lua','ruby','brainfuck']
    print(sorted(li))#預設照第一個字母來排列順序,如相同再來比較之後字母，以此類推
    print(sorted(li,key=k))#變更排列方式，以長度來排，如果長度相同，誰先在list中出現就先排
    data =[('Andre',33),('Johnnny',25),('Bob',13)]
    print(sorted(data))#預設以第一個元素來排列
    print(sorted(data,key=k1))#變更以第二個元素排列
    print(sorted(data, key=k3))#變更以第一個元素的長度來排列
