def group(iterable,size):
    return [li[i:i+size] for i in range(0,len(list(iterable)),size)]

# def group(iterable, size):
#     result = []
#     it = iter(iterable)
#     while True:
#         temp = []
#         try:
#             for i in range(size):
#                 temp.append(next(it))
#             result.append(temp)
#         except StopIteration:
#             if temp != []:
#                 result.append(temp)
#             break
#     return result

if __name__ == '__main__':
    # simple tests
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if group(li, 3) != [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]:
        print('Failed')
    if group(li, 4) != [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]:
        print('Failed')
    if group(li, 1) != [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]:
        print('Failed')
    if group(li, 3) != [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]:
        print('Failed')
    if group(li, 4) != [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]:
        print('Failed')
    if group(li, 1) != [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]:
        print('Failed')