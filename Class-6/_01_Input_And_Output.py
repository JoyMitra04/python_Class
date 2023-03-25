# Display Process-1

print("Hello Python")
print("Python", end=" and")
print(" ", "Java")

# Display Process-2

language = "Python"
print("Hello:", language, "and Java")

# Display process-3

Country = "Bangladesh"
Country2 = "USA"

print("country one is: {} and country two is: {}".format(Country, Country2))
print("country one is: {c2} and country two is: {a1}".format(a1=Country, c2=Country2))

# Display process-4

print(f"country are {Country} and country {Country2}")
print(f'country are {Country2} and country {Country}')

# Display process-5

"""
%f= float
%d= int
%s= string
"""
num = 10.123456789

print("%.4f" % num)
print("%d" % num)
print("%.4s" % Country)
print("country one is %s and country two is %s" % (Country, Country2))

names = ["Shamim", "Shahi", "Habib"]
names.pop(1)
print(names)


