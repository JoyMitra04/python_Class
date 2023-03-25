"""
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also
create a lambda function that multiplies argument x with argument y and prints the result.


add = lambda num: num + 15
print(add(10))

mul = lambda x, y: x * y
print(mul(12, 4))
""""""
2. Write a Python program to create a function that takes one argument, and that argument will be multiplied 
with an unknown given number.


def fun_mul(n):
    return lambda num: num * n

result = fun_mul(2)
print("Double the number of 15 =", result(15))
result = fun_mul(3)
print("Triple the number of 15 =", result(15))

# 5. Write a Python program to filter a list of integers using Lambda.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_lst = filter(lambda num: num % 2 == 0, lst)
odd_lst = filter(lambda num: num % 2 != 0, lst)

print(list(even_lst))
print(list(odd_lst))

# 6. Write a Python program to square and cube every number in a given list of integers using Lambda.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sqr_lst = map(lambda num: num ** 2, lst)
cube_lst = map(lambda num: num ** 3, lst)
print(list(sqr_lst))
print(list(cube_lst))

# 7. Write a Python program to find if a given string starts with a given character using Lambda.
start_with = lambda x: True if x.startswith("p") else False

print(start_with("python"))
start_with = lambda x: True if x.startswith("p") else False
print(start_with("Java"))
"""

