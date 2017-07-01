#判別是否為重組字，重組字是兩個字串是以相同字母用不同排列組成，不管大小寫和空白
def is_anagram(s1,s2):#s1,s2為兩字串
    s1 = "".join(s1.lower().split())#先全部小寫後以空白分割成以字母組成的list，在合併成一個字串
    s2 = "".join(s2.lower().split())

    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    print(is_anagram("heart","earth"))
    print(is_anagram("Torchwood","Doctor Who"))
    print(is_anagram("computer", "cuter mop"))
    print(is_anagram("stop", "spot"))
    print(is_anagram("listen", "silent"))
    print(is_anagram("William Shakespeare", "I am a weakish speller"))