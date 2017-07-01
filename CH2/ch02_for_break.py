scores=(98,78,64,55,61,82)
lower_than_60 = False
for x in scores:
    print(x)
    if x< 60:
        print("Lower than sixty")
        lower_than_60= True
        break
