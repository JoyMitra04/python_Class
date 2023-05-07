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
    weight = None

    # Instance Method
    def getDetails(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.height)
        print(self.weight)
        print(".............")

hasan = Person()
hasan.name = "Hasan Mahamud"
hasan.age = 100
hasan.gender = "Male"
hasan.height = 5.9
hasan.weight = 65

arafat = Person()
arafat.name = "Arafat Hassan"
arafat.age = 80
arafat.gender = "Male"
arafat.height = 5.6
arafat.weight = 80

hasan.getDetails()
arafat.getDetails()