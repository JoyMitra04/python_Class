"""
Read an integer N and compue all its divisors.
input
The input file contains an integer value.
output
write all positive divisors of N, one value per line.



N = int(input())
start = 1
while start <= N:
    if N % start == 0:
        print(start)
    start += 1


N = int(input())
for num in range(1, N+1):
    if N % num == 0:
        print(num)
"""
