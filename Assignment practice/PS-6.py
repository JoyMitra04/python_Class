# 6. Write a Python program to check whether a year is leap year or not.

year = int(input())

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print("leap year")

else:
    print("not leap year")