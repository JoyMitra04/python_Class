"""
def sum_tail_recursion(num, sum=0):
    if num == 0:
        return sum
    else:
        return sum_tail_recursion(num - 1, sum + num)
print(sum_tail_recursion(5))

sum = 0
def sum_tail_recursion(num):
    global sum
    if num == 0:
        return sum
    else:
        sum += num
        return sum_tail_recursion(num - 1)
print(sum)
print(sum_tail_recursion(5))
print(sum)
"""

# 1. Write a head-recursive and tail-recursive function to calculate the mathanosto-factorial of a given a number.
# [5! = 120 || even number || [2*4 = 8]]

# 2. Implement a head-recursive and tail-recursive function to find the maximum element in the List.
# 3. Implement a head-recursive and tail-recursive function to find the minimum element in the list.



