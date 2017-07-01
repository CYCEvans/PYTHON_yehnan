import ch4_11
def matrix_m(m1, m2):
    li = []
    if len(m1[0]) != len(m2):
        return "不能相乘"
    else:
        li = ch4_11.matrix_create(len(m1),len(m2[0]),0)#先產生相乘後的二維list(矩陣)
        # for x in range(len(m1)):
        #     li.append([])
        #     for y in range(len(m2[0])):
        #         li[x].append(0)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    li[i][j] += m1[i][k] * m2[k][j]

    return li

if __name__ == "__main__":
    m1 = [[1, 2],[2, 4],[4, 1]]
    m2 = [[2, 3 ,1 ,2],[3, 1, 1, 2]]
    print(matrix_m(m1, m2))