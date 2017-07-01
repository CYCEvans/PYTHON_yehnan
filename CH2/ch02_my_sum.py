def my_sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


scores0 = [60,73,81,95,34]
scores1 = [10,20,30,40,50,60,70]

print(my_sum(scores0))
print(my_sum(scores1))