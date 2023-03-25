"""
start = 1
end = 10
sum = 0

while start < end:
    num = int(input("enter number:"))
    sum += num
    start = start + 3
    print(sum)


even_sum = 0
odd_sum = 1
start = 1
end = int(input())


while start <= end:
    num = int(input())

    even_sum += num
    odd_sum += num
    start += 1
    print(even_sum)
    print(odd_sum)

if even_sum % 2 == 0 and even_sum > odd_sum:
    print("even winner")

elif odd_sum % 2 != 0 and odd_sum > even_sum:
    print("odd winner")

else:
    print("Out of Context")
"""

