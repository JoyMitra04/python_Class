class A:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

class B(A):
    def __init__(self, name, age):
        A.__init__(self, name)
        self.age = age

    def getage(self):
        return self.age

class C(B):
    def __init__(self, name, age, country):

        B.__init__(self, name, age)
        self.country = country

    def getcountry(self):
        return self.country

Object_C = C("Joy Mitra", 20, "Bangladesh")
print(Object_C.getname())
print(Object_C.getage())
print(Object_C.getcountry())




