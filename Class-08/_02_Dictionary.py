"""
-key: Value pairs
-Unordered
-{}
[0]: "python"
[1]: "python"
"""

#Empty Dictionary

my_dict = {}
print(type(my_dict))

my_dict_2 = dict()
print(my_dict_2)

# With value

my_dict_3 = {"name": "Joy Mitra",
             "fav_language": "python",
             "one": 1,
             "two": 2.5,
             "lst": [1, 2, 3, 4]
             }

print(my_dict_3)

# Access
print(my_dict_3["name"])
print(my_dict_3["fav_language"])
print(my_dict_3["one"])
print(my_dict_3["two"])
print(my_dict_3["lst"])
print(my_dict_3["lst"])

my_dict4 = {1: 1, 2: 5.5, }
print(my_dict4.get(2))

# Update / add

my_dict4[1] = "one"
print(my_dict4)

my_dict4[2] = "two"
print(my_dict4)

# Remove
print(my_dict4.pop(1))
print(my_dict4.pop(2))

my_dict_3.clear()
print(my_dict_3)
