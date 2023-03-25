# 9. Write a Python program to input any character and check whether it is alphabet, digit or special character.

cha = input()

if cha.isalpha():
    print("alphabet")

elif cha.isdigit():
    print("digit")

else:
    print("Special character")

