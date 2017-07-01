scores = [60,73,81,95,34]
n = 0
high_total = 0
for x in scores:
    if x < 60:
        continue
    n+=1
    high_total +=x

print(n)
print(high_total)