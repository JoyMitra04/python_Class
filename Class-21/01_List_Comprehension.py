lst = [1, 2, 3, 4, 5]

# List_Comprehension
lst_comp = [num for num in range(1, 6)]
print(lst_comp)

even_lst_comp = [num for num in range(1, 101) if num % 2 == 0]
print(even_lst_comp)

lst = []
for num in range(1, 4):
    if num % 2 == 0:
        lst.append(num)
print(lst)
