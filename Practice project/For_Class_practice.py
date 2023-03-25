"""
start = 1
end = int(input())
sum = 1
while start <= end:
    sum *= start
    print(sum)
    start += 1

lst = [1, 2, 3, 4]
start = 0
end = len(lst)
sum = 0

while start < len(lst):

    sum += lst[start]
    start += 1
    print(sum, end=",")


lst = [1, 3, 4, 5]
start = 0
end = len(lst)
sum = 0

while start < end:
    sum += lst[start]
    if sum == 8:
        break
    start += 1
    print(sum, end=",")

"""








