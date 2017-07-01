#找出 a b c 中最大的
a,b,c = 3,5,7
x=None
if a < b:
    if c > b:
        x = c
    else:
        x = b
else:
    if c > a:
        x = c
    else:
        x = a

x
print(x)