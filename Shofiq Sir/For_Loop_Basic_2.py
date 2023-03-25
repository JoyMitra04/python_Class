"""
J = "JOy mitra"
for joy in J :
    print(joy)

for joy in range(4, 11, 2):
    print(joy, end=" ")
print("\n")

# How to print odd number with for loop
for joy in range(1, 11, 2):
    print(joy, end=" ")
print("\n")

# How to print even number with for loop
for joy in range(0, 11, 2):
    print(joy, end=" ")


# For loops part two

for i in range(1, 101):
    print(i)

# for i membership iterative/ sequince

# Decrease with for loops
for joy in range(10, 4, -1):
    print(joy)


sum = 0
for i in range(1, 51, 1):
    sum += i
print(sum)

lst = [1, 2, 3, 4]
sum = 0
for i in lst:
    sum += i
print(sum)

lst = list(range(1, 10, 2))
print(sum(lst))
sum = 0
for i in lst:
    sum += i
    print(sum)

# multiplication with for loop
for i in range(1, 4):
    print(i * i)

for i in range(1, 4):
    print(i, "^", 2, "=", (i * i))

sum = 1
for i in range(2, 5):
    sum *= i
    print(sum)

lst = [1, 2, 3, 4]
sum = 1
for i in lst:
    sum *= i
print(sum)

# Numta with for loop
for i in range(1, 11):
    print(2, "X", i, "=", (i * 2))

numta = int(input())
for i in range(1, 11):
    print(f"{numta},X,{i},= {numta * i}")

# Nested for loop
for i in range(4):
    for i2 in range(10, 18):
        print(i, i2)

for i in ["joy", "mitra"]:
    for j in ["apple", "mango"]:
        print(i, "eats", j)

person = ["JOY", "Mitra"]
for i, j in enumerate(person):
    print(i, j)

for i in range(5):
    print("*"*i)
"""
