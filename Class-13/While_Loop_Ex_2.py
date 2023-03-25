lst = [10, 20, 23, 30, 50]

start = 0
end = len(lst)

while start < end:
    value = lst[start]
    start += 1

    if value % 2 == 1:
        continue

    else:
        print(value)
