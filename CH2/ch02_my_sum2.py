def my_sum(numbers,initial=0): #通常預設為0，這樣只要設一個參數即可
    total = initial
    for x in numbers:
        total += x
    return total


scores0 = [60,73,81,95,34]
scores1 = [10,20,30,40,50,60,70]

print(my_sum(scores0,100))#從100開始往上加
print(my_sum(scores1))#只設一個參數，代表從預設開始加上去