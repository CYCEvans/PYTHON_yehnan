s = "hello python welcom"
s = s.capitalize()
print(s)
print(s.title())
print(s.istitle())
print(s.find("s"))
# print(s.index("s"))#跟find 一樣，但find找不到會回傳-1，index會回傳ValeError
print(s.index("o"))
print(s.rfind("o"))
print(s.count("o"))
print('a'.isidentifier(),"0123ab".isidentifier())#識別字為變數名稱，不能以數字開頭
print("abc".isprintable(),"a\nb\tc".isprintable())#可視字元是可印出
s2 = "Hello, Python, Hi "
print(s2.partition(','))#從第一個開始切割
print(s2.partition(', P'))
print(s2.partition('X'))#沒有在字串中會切成本體和兩個空字串
print(s2.rpartition(','))#從最大index開始切割
li = ["Hello","Python","Hi"]
s3 = ' '.join(li)#字串結合可迭代的物件
print(s3)
r = reversed(s3)#為一可迭代的reversed物件
print(''.join(r))#結合join 印出字串倒數
print(s3[::-1])#切片可輸出同樣結果
