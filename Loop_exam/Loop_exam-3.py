"""
Read an integer N. Print all number between 1 and 40, which divided by will give the remainder is 2.
print all numbers between 1 and 40, which divided by N will give the remainder is 2, one per line.

"""
N = int(input())


for number in range(1, 41):
    if number % N == 2:
        print(number)
