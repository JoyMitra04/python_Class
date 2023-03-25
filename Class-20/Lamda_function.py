"""
1. Lambda functions in python
2. Comprehensions in python
"""

"""
- Normal Function 
def functionName(Parameters):
// statements - 1
// statements - 2
// statements - 3

- Lambda Function 
    - Anonymous Function / Unnamed Function
    - lamda keyword 
    - single statementv   


# Normal Function
def add100WithTheArgument(num):
    return num + 100
print(add100WithTheArgument(10))

# Lambda Function Syntax - lambda arguments : expression
add = lambda num: num + 100
print(add(10))

# Filter(function, iterable)

lst = [34, 12, 64, 55, 75, 13, 63]
odd_lst = filter(lambda num: num % 2 == 1, lst)
print(list(odd_lst))

# Map
lst = [1, 2, 3, 4, 5]
sqr_lst = map(lambda num: num ** 2, lst)
print(list(sqr_lst))

sqr_lst_logical = map(lambda value: value + 10 if value % 2 == 0 else value + 5, lst)
print(list(sqr_lst_logical))
"""
# https://git-scm.com/
# Write a Python Program to count even and Odd in a List of Integers using Lambda Function.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count_even = filter(lambda num: num % 2 == 0, numbers)
count_odd = filter(lambda num: num % 2 == 1, numbers)

print(len(list(count_even)))
print(len(list(count_odd)))


# Write a Python Program to count even and Odd in a List of Integers using Lambda Function.list user input


