def matrix_create(m,n,init=None):
    li = []
    for x in range(m):
        li.append([])
        for y in range(n):
            li[x].append(init)
    return li
if __name__ == "__main__":
    print(matrix_create(2,3,"x"))