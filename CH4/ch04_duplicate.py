#找出有重複的元素
def dupclite(iterable):
    fst=[]
    snd=[]
    for x in iterable:
        if x not in fst: # 第一次出現加入這個list
            fst.append(x)
        elif x not in snd:#第二次出現的加入這個list
            snd.append(x)
        else:#三次出現以上就不處理
            pass
    return snd
if __name__ == '__main__':
    lst = [4,8,9,5,7,2,1,7,4,9,8,5]
    print(dupclite(lst))
