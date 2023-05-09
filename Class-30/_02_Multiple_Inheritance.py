class A:
    def __init__(self):
        self.fatherName = "Nitai Mitra"
        print("A class")

class B:
    def __init__(self):
        self.motherName = "Anjana Mitra"
        print("B class")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    print("C class")

    def getDetails(self):
        print(self.fatherName, self.motherName)

Object_C = C()
Object_C.getDetails()