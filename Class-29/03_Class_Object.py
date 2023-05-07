"""
1. Class
2. Object
3. Attribute

4. Constructor
5. Instance Method
"""

class Person:
    # Attribute
    name = None
    age = None
    gender = None
    height = None

    # Constructor
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height


    # Instance Method
    def getDetails(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.height)
        print(".............")

hasan = Person("Hassan", 80, "Male", 5.9)
arafat = Person("arafat", 100, "Male", 5.6)

hasan.getDetails()
arafat.getDetails()
"""
class Person:
    name = None
    age = None
    gender = None
    height = None

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def getDetails(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Height: ", self.height)

obj = Person('Ajay', 28, 'Male', 6.0)

obj.getDetails()
"""