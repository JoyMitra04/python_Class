file_data = open("demo.txt", "r")
print(file_data.read())

file_data = open("demo.txt", "w")
print(file_data.write("Hello World!"))

file_data = open("demo.txt", "a")
print(file_data.write("\nHello Mother fuckers!"))
file_data.close()

with open("demo.txt") as d:
    print(d.read())