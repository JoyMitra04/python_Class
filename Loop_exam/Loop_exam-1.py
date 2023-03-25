"""
num_of_input = int(input())
lst = []
start = 0

while start <= num_of_input:
    number = int(input())
    lst.append(number)
    start += 1


index = 0
while index <= num_of_input:
    if lst[index] > 120:
        break
    elif lst[index] % 10 == 0:
        print(lst[index])
        index += 1




Given a list(must be user input) iterate it and display numbers which are divisible by 10 and if you find
number greater than 120 stop the loop iteration




number_of_input = int(input())
lst = []
start = 0

while start <= number_of_input:
    number = int(input())
    lst.append(number)
    start += 1

index = 0
while index <= number_of_input:
    if lst[index] > 120:
        break
    elif lst[index] % 10 == 0:
        print(lst[index])
        index += 1
"""
# Solve with Chat gpt
# take user input for list
lst = input("Enter a list of numbers, separated by spaces: ").split()

# convert list of strings to list of integers
lst = [int(i) for i in lst]

# iterate through the list using a while loop
i = 0
while i < len(lst):
    # check if the number is divisible by 10 and less than or equal to 120
    if lst[i] % 10 == 0 and lst[i] <= 120:
        print(lst[i])
    # stop the loop iteration if the number is greater than 120
    elif lst[i] > 120:
        break
    i += 1

