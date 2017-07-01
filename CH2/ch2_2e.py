for x in range(1,10):
    for y in range(1,10):
        print('%d * %d = %d' % (x, y, x*y))
    
x=1

while x<10:
    y=1
    while y<10:
        print('%d * %d = %d' % (x, y, x*y))
        y += 1
    x += 1
