def teacher(li):
    result = []
    for n in li:
        if n < 60:
            result.append(n)
    return result
def teacherb(li):
    return [x for x in li if x < 60]
if __name__ == "__main__":
    lst = [70,88,60,58,43,28,13,55,89,16,37,52]
    print(teacher(lst))
    print(teacherb(lst))