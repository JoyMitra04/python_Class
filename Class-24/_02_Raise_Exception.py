num1 = int(input())

if num1 % 2 != 0:
    raise Exception("shoudn't be odd number.")
else:
    print("num1 is even number")
