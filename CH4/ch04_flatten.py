# 壓平二維list便一維list，一定要全部以二維串列為元素組成的list
def flatten(list2d):
    result=[]
    for x in list2d:
        result.extend(x)#extend只能代入迭代性物件
    return result
if __name__ == '__main__':
    lst = [[4,8,9],[5],[7,2],[11,7,4],[9,8,5]]
    print(flatten(lst))
    lst = [(4, 8, 9), [5], (7, 2), [11, 7, 4], [9, 8, 5]]
    print(flatten(lst))