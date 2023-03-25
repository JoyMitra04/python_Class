"""
1. Start
2. End - (input(): from user)
3. Value -> even / odd
4. Odd sum -> Odd
5. evensum -> even
6. print(oddsum <  envensum) - Even winner/ odd winner
"""

start = 1
end = int(input())
evensum = 0
oddsum = 0
while start <= end:
    evensum += start
    oddsum += start
    start += 1


if evensum % 2 == 0 and evensum > oddsum:
    print("Even winner")

elif oddsum % 2 != 0 and oddsum > evensum:
    print("odd winner")

else:
    print("Both are equal")
