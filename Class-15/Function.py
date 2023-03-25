# Parameters / Argument
# No Argument Function and Argument Function
# Void function
# Library / Builtin Function
# User Defined Function
"""
def getMaxNum(Num1, Num2):

    if Num1 > Num2:
        return
    elif Num2 > Num1:
        return


def getMinNum(num1, num2):

    if num1 > num2:
        return
    elif num2 > num1:
        return


def divTwoNum(num1, num2):
   return  num2 / num1


# Void Function
def printMessage():
    print("hello world")

msg = printMessage()
print(msg)

a = 100
b = 200
result = getMaxNum(a,b)
print(result)

a = 200
b = 300
print(getMaxNum(a, b))


def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def expo(num1, num2):
    return num1 ** num2

def Divide(num1, num2):
    return num1 / num2

def Fdivision(num1, num2):
    return num1 // num2

def rem(num1, num2):
    return num1 % num2

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

result = add(num1, num2), sub(num1, num2), mul(num1, num2), expo(num1, num2), Divide(num1, num2), rem(num1, num2)

print(result)



"""

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

print("Please select operator")
print("1. add")
print("2. sub")
print("3. mul")
print("4. div")
choice = input("Enter choice(1/2/3/4)= ")


num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == "2":
    print(num1, "-", num2, "=", sub(num1, num2))

elif choice == "3":
    print(num1, "*", num2, "=", mul(num1, num2))

elif choice == "4":
    print(num1, "/", num2, "=", div(num1, num2))

else:
    print("invalid arguments")



