"""
file = open("demo.txt", "r")

file_content = file.read()
New_file_content = file_content.replace("Hello World!", "Hello Mother Fuckers")
print(New_file_content)

file.close()

file = open("demo.txt", "w")
file.write(New_file_content)
file.close()
"""
