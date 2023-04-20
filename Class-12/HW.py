"""
start = 1
end = int(input())
result = 1

while start <= end:

    result = (result * start)
    start = start + 1
    print(result)


lst = [10, 20, 30, 40, 50]
start = 0
end = len(lst)

while start < end:
    if lst[start] == 40:
        break
    print(lst[start])

    start = start + 1
"""
num_of_input = int(input())
lst = []
start = 0

while start <= num_of_input:
    number = int(input())
    lst.append(number)
    start += 1


index = 0
while index < num_of_input:
    if lst[index] > 120:
        break
    elif lst[index] % 10 == 0:
        print(lst[index])
        index += 1

