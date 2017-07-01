# 計算總分與平均
scores = [60,73,81,95,34]
n = 5
sum = 0
count = 0
while count < n:
    sum += scores[count]
    count += 1

avg = sum/count
print(avg)
