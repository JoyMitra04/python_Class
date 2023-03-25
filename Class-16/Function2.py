## Types of Arguments
### 01. Default arguments
### 02. Keyword arguments
### 03. Variable_lenth arguments[*args/ **kwargs]
"""
# Type - 01

def add(num1, num2=0):
    return num1 + num2

add(10, 20)
add(10)

# Type - 02

def getstudentName(firstname, lastname):
    print(firstname, lastname)

getstudentName("JOY", "Mitra")
getstudentName(lastname="Joy", firstname="mitra")

# Type - 03

def add(*numbers):
    #print(numbers)
    sum = 0
    for num in numbers:
        sum += num
    print(sum)
add(10, 20)
add(10, 100, 40)

# Type - 04

# keywords argument
def getKeyValue(**kwargs):
    print(kwargs)

    for key, value in kwargs.items():
        print(key, value)


getKeyValue(Firstlanguage="Python", Secondlanguage="Java")

# Type - 01

def add(num1, num2 = 0):
    return num1 + num2

print(add(10, 20))
print(add(10))
result = add(100, 200)
print(result)

# Type - 02

def getStudentName(fastname, lastname):
    print(fastname, lastname)

getStudentName("JOy", "Mitra")
getStudentName(fastname="mitra", lastname="JOy")

# Type - 03

def getStudentIdentity(*details):
    return details

print(getStudentIdentity("Name: JOY MITRA", "Roll: 3316", "Batch: 49"))

def add(*nums):
    sum = 0
    for numbers in nums:
        sum += numbers
    print(sum)

add(10, 20, 30, 40, 100)


def getStudentIdentity(**details):
    #print(details)

    for keyvalue in details.items():
        print(keyvalue)

getStudentIdentity(name = "Joy", roll = 3316, Batch = 49)
"""

