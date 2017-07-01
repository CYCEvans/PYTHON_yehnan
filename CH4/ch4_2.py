def list_sep(iterable,size):
    result = []
    li = list(iterable)
    length=len(li)
    for i in range(0,length,size):
        result.append(li[i:i+size])
    return result
def list_sep2(iterable,size):
   return [(li[i:i + size]) for i in range(0, len(list(iterable)), size)] #用串列生成式

if __name__ == '__main__':
    # simple tests
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list_sep(li, 3))
    print(list_sep2(li, 3))
    if list_sep(li, 3) != [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]:
        print('Failed')
    if list_sep(li, 4) != [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]:
        print('Failed')
    if list_sep(li, 1) != [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]:
        print('Failed')

    if list_sep2(li, 3) != [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]:
        print('Failed')
    if list_sep2(li, 4) != [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]:
        print('Failed')
    if list_sep2(li, 1) != [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]:
        print('Failed')


