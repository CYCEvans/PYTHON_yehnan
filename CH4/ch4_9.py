strs = "abcdefghijklmnopqrstuvwxyz"
def rangeStr(start=None, end=None,step=1):
    result = []
    if end == None:
        inxEnd = strs.index(start)
        for i in range(inxEnd):
            result.append(strs[i])
    else:
        inxStart = strs.index(start)
        inxEnd = strs.index(end)
        for i in range(inxStart,inxEnd,step):
            result.append(strs[i])
    return result

if __name__ == "__main__":
    print(rangeStr('f'))
    print(rangeStr('i','l'))
    print(rangeStr('a','f',2))
    
