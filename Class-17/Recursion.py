# Recursion
"""
-Recursion is a programming technique in which a *function* calls itself one or more times to solve a problem.
- Two Parts: 1. Base Case and 2. Recursive case


- A loop is control structure that iteratively executes a block of code until a certain condition is met.
- Recursion, is a technique in which a function calls itself to solve a problem.

- Recursion can be less efficient than loop
"""
"""
for cnt in range(countDown):
    print("Hello world!")
"""
"""
countDown = int(input())

def countDownString(cnt):
    # Base Case
    if cnt == 0:
        pass
    else:
        print("hello world!")
        countDownString(cnt - 1)
        
# Function Call
countDownString(countDown)


def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)
    print(n)

head_recursion(10)

# Graph Algorithm / Tree algorithm
"""

def getsum(n):
    if n != 0:
        return n + getsum(n-1)
    else:
        return n

num = int(input())
print(getsum(num))




