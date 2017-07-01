ft = [32,212,10,55,78,110,178]
ct = [(x-32)*5/9 for x in ft]#串列生成式
print(ct)
#--------其他串列產生式試做-------
li = [32,55,-78,58,-92,32,-87]
li2 = [abs(x)for x in li]
print(li2)#絕對值
print([x*2 for x in range(1,11)])#兩倍,沒有被[]包起來就是個generator
li = [(30,41,65),(60,70,80),(95,78,65,88)]
print([sum(x)/len(x) for x in li ])
li=['apple','cake','candy','lollipop']
print([(x,len(x)) for x in li]) #產生tuple的元素
li = ['a.jpg','b.png','c.bmp','end.jpg','fox.py','gogl.java']
print([x for x in li if x[-4:] == '.jpg'])#找出是jpg檔案
li = [[x*2 for x in range(6)],[x*2+1 for x in range(6)]]
for x in [y for x in li for y in x if y<10]:#generator可以放入list或是直接由for來迭代
	print(x)