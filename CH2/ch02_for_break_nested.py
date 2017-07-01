data=[[33,44,55],[18381,99781],[60,70,101,91],[32,51]]
total = 0
for x in data:
    for y in x:
        if 0 <= y <= 100:
            total +=y
        else:
            break

print(33+44+55+60+70+91+32+51)
print(33+44+55+60+70+32+51)
print(total)