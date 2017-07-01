# -*- coding: utf-8 -*-
def plateau(data):
    if len(data) == 0: #先扣掉空list
        return None
    data.sort()       #先整理順序
    max = data[0]     #假設最大值是第一個元素
    count_max = 1     #最大值出現次數預設為1
    count_other = 0   # 其他值計數預設為0
    for i in range(1, len(data)):#從第一個元素開始迭代
        other_last = data[i - 1] # 上一個元素值
        otherx = data[i] # 其他值
        if data[i] == max:   #若元素 等於最大值，最大次數加1
            count_max += 1
        else: #出現不是最大元素後，開始計算在其他值
            if otherx != other_last: #如果與上一個元素不一樣，開始預設計算值為1。
                count_other = 1
            else:
                count_other +=1    #如果與上一個元素一樣，開始往上增加。
        if count_other > count_max: #假設其他數大於最大值，替換最大值
            max, count_max = otherx,count_other
            count_other = 1
            
    return max
if __name__ == '__main__':
    # simple tests
    data = [0, 1, 1, 2, 3, 4, 5, 5, 9, 9, 9, 23, 25, 25, 25]
    if plateau(data) != 9:
        print('Failed')

    data = [1, 1, 1, 2, 3, 4, 5, 5, 9, 9, 9, 23, 25, 25, 25]
    if plateau(data) != 1:
        print('Failed')

    data = [1, 1, 1, 2, 3, 5, 5, 5, 5, 9, 9, 23, 25, 25, 25]
    if plateau(data) != 5:
        print('Failed')

    data = [0, 1, 1, 2, 3, 4, 5, 5, 9, 9, 9, 23, 25, 25, 25, 25]
    if plateau(data) != 25:
        print('Failed')

    data = [0, 1, 2, 3, 3, 4, 5, 5, 9, 9, 9, 23, 25, 25, 25, 25, 26, 27, 27]
    if plateau(data) != 25:
        print('Failed')

