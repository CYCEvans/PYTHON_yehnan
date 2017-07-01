def trans(r):
    if r < 0: #transform to 0;255
        r = 0
    elif r > 255:
        r = 255
    if 200<=r <= 255:
        r = int(100+(r-255)*15.0/55.0)
       
    elif 0 <= r <= 130:
        r = int(60+ (r-130)*6.0/13.0)
        
    else:
        r = int(84 + (r-199)*23.0/68.0)
    return r
if __name__ == '__main__':
    # simple tests
    if trans(0) != 0:
        print('Failed')
    if trans(130) != 60:
        print('Failed')
    if trans(200) != 85:
        print('Failed')
    if trans(255) != 100:
        print('Failed')
