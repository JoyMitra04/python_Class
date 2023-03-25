"""
Set:
1. Unordered
2. Unindex
3. Duplicate not allow

Tuple:
1. Ordered
2. unchangeable
3. Allow duplicate data
List:
1. ordered
2. changeable
3. Allow duplicate data

"""



# my_set = {}
# print(type(my_set))

my_set_2 = set ("python")
print(type(my_set_2))
print(my_set_2)

a = (1, 2, 3, 4)
print(type(a))

my_set_2 = {1, 2, 3, 1, 2, 3, 4}
print(my_set_2)

my_set_3 = set("1")
print(my_set_3)
print(type(my_set_3))


#Union Operation

A = {1, 2, 3, 4, 5}
B = {1, 6, 7, 8, 9, 10}

print(A | B)
print(A.union(B))

# Intersection
print(A & B)
print(A.intersection(B))

