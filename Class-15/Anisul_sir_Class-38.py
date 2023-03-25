def student(*details):
    print(details)

student(101, "Joy", 3.92)


def add(*numbers):
    sum=0
    for num in numbers:
        sum += num
    print(sum)

add(10, 20, 30, 4.4)

def student(**details):
    print(details["name"])

student(id=3316, name = "Joy", Gpa= 3.92)

