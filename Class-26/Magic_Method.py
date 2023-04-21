# Arithmetic_Operators

num1 = 10
num2 = 20

# num_2 = num1 + num2

add = num1.__add__(num2)
print(add)

sub = num1.__sub__(num2)
print(sub)

mul = num1.__mul__(num2)
print(mul)

trudiv = num1.__truediv__(num2)
print(trudiv)

floordiv = num1.__floordiv__(num2)
print(floordiv)

mod = num2.__mod__(num1)
print(mod)

pow = num1.__pow__(2)
print(pow)

le = num1.__le__(num2)
print(le)

ge = num1.__ge__(num2)
print(ge)

print(num1.__eq__(num2))
print(num1.__ne__(num2))
print(num1.__lt__(num2))
print(num1.__gt__(num2))

a = True
b = False

print(a.__and__(b))
print(a.__or__(b))

lst =[1, 2, 3, 4, 5]
print(lst.__contains__(5))