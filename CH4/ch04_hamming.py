def hamming(s1,s2):#漢明距離即是兩字串的差別
    lens = (len(s1),len(s2))#先查兩個字串的長度
    minlen = min(lens)
    maxlen = max(lens)
    h = maxlen- minlen #長度相差多少，就是需要改變的次數

    for i in range(minlen):#以最短的字串長度迭代出index list
        if(s1[i] != s2[i]):#比較兩字串各字元，不一樣就要多改變一次
            h +=1
    return h

if __name__ == "__main__":
    print(hamming("abc","abcde"))
    print("------------")
    print(hamming("decba","abcde"))
    print("------------")
    print(hamming("abcdsef","ccdda"))
