# 2. Write a Python program to find maximum between three numbers.

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 or num1 > num3:
    print("num1 is greater than num2 or num3")

elif num2 > num1 or num2 > num3:
    print("num2 is greater than num1 or num3")

else:
    print("num3 is greater than num1 or num2")