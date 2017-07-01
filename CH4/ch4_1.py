def only_one_num(iterable):
    fst = []
    for x in iterable:
        if x not in fst:
            fst.append(x)
        else:
            fst.remove(x)
    return fst
if __name__ == "__main__":
    lst = [9,5,5,-4,7,6,4,1,-2,0,10,9,7]
    print(only_one_num(lst))
    li = [1, 1, -3, -3]
    if only_one_num(li) != []:
        print('Failed')
    li = [5, 6, 8, -3]
    if only_one_num(li) != [5, 6, 8, -3]:
        print('Failed')
    li = [-3, 8, 5, 6, 8, -3]
    if only_one_num(li) != [5, 6]:
        print('Failed')
