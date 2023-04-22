"""
-Generator Function
-Normal Function: return // Generator Function: yield


def lst(list):
    return list

list = [1, 2, 3, 4]
print(lst(list))
"""
def generator_function():
    yield "Hello Python"
    yield [1, 3, 5]
    yield [1, 2, 3, 4]

func = generator_function()
print(func)
print(next(func))
print(next(func))
print(next(func))
