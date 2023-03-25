"""
i = 1
while i <= 100:
    print(i)
    i += 1

# How to find even number
i = 2
while i <= 100:
    print(i)
    i += 2

# How to find odd number
i = 1
while i <= 100:
    print(i)
    i += 2


# How to print horizontal.

i = 1
while i <= 10:
    print(i, end=" ")
    i += 1

# How to + all numbers.
sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
    print(sum)

fast = int(input("Fast number="))
last = int(input("Last number="))
diff = int(input("diff="))
sum = 0

while fast <= last:
    print(fast, end=" ")
    sum = sum + fast
    fast += diff
print('\n', sum)

i = 1
while i <= 3:
    print("Python")
    i += 1
    j = 1
    while j <= 5:
        print(j)
        j += 1

# How to
i = 1
while i <= 10:
    print(4, 'X', i, "=", (i * 4))
    i = i + 1

numta = int(input())
i = 1
while i <= 10:
    print(f"{numta} X {i} = {numta*i}")
    i += 1

i = 1
while i <= 10:

    j = 1
    while j <= 10:
        print(f"{i} X {j} = {i * j}")
        j += 1
    i += 1


i = 1
while i <= 4:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    i += 1
    print("\n")
"""
