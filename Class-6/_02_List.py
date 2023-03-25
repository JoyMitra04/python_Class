"""
List:

1. Ordered
2. Element access by index
3. Mutable type data structure
4. Various type data - integer/ float / list / others

"""

# Declare - empty

lst = []
print(type(lst))

lst_2 = list()
print(type(lst_2))

# Declare - Value

lst_3 = [28, 4, 31, 4.28, "Mitra", [4, 31, "Joy"]]

print(type(lst_3))  # <class 'int'>
print(lst_3)

# Access Element

print(lst_3[2])
print(lst_3[-2])
print(lst_3[:6])
print(lst_3[4:])
print(lst_3[5][2])

# Length

print(len(lst_3))

# Adding

lst_3.append(28)
print(lst_3)

lst_3.insert(0, '04')
print(lst_3)

lst_4 = [1, 2, 3, 4, ]
lst_3.extend(lst_4)
print(lst_3)

lst_3.reverse()
print(lst_3)

# Value Update - Mutable

lst_3[0] = "Joy Mitra"
print(lst_3)

# Remove

lst_3.remove(28)
print(lst_3)

lst_3.pop(9)
print(lst_3)



