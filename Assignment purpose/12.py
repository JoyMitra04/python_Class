# Given a list(Must be user input)iterate it and display numbers which are divisibly by 10 and if you find number greater then 120 stop the loop
# iteration.

num_of_input = int(input())

num_list = []
start = 0

while start <= num_of_input:
    number = int(input())
    num_list.append(number)
    start += 1

index = 0

while index <= num_of_input:

    if num_list[index] > 120:
        break
    elif num_list[index] % 10 == 0:
        print(num_list[index])
        index += 1

































