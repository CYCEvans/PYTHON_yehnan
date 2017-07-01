#99乘法表
result=[]
# for x in range(2,10):#原本的方式
#     for y in range(2,10):
#         result.append("{} * {} = {}".format(x,y,x*y))
result=["{} * {} = {}".format(x,y,x*y) for x in range(2,10) for y in range(2,10)]
print(result)