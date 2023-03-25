list = int(input())
start = 1
end = len(list)
sum = 0

while start <= end:
    sum += start
    start += 1
    print(sum)