scores = [30,99,41,55,84]
print("old scores: ",scores)
scores_new=[]
for x in scores:
    if x >= 90:
        scores_new +=[x]
    elif x+10 >90:
        scores_new +=[90]
    else :
        scores_new +=[x+10]

print("new scores: ",scores_new)
