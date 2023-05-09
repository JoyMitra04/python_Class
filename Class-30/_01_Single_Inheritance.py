"""
## Inheritance
- Reusability
"""

# Single Inheritance

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(self.name)
        print(self.age)

class B(A):
    def __init__(self, name, age, salary, designation):

        self.salary = salary
        self.designation = designation

        A.__init__(self, name, age)

    def display_details_B(self):
        print(".............")
        print(self.name)
        print(self.age)
        print(self.salary)
        print(self.designation)
        print(".............")


a = A("Joy Mitra", 20)
b = B("Joy Mitra", 20, "Unempolyed", "Nothing")
a.display_details()
b.display_details_B()
b.display_details()

