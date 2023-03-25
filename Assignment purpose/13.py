"""

[1, 2, 3,  4]


[1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4 ]

Output - [ 1, 3, 6, 10]
------------------------------------------------------------

[1, 1, 2, 4]

output - [1, 2, 4, 8]

------------------------------------------------------------
1. Base While Loop  -> Current Index [3]
2. Inner While Loop  -> Left Index [0, 1, 2]
"""

"""
Given a list of nums.
We define a running sum of a list as runningsum[i] = sum (num[0]........sum[i]).
Return the running sum of nums.
"""


""""""
start = 1
end = int(input())
result = 0

while start <= end:
    result = (result + start)
    start += 1

    print(result)


