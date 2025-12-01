# """1. arithmatic operations:"""
# #modulus(%):
# x = float(input("enter numerator:"))
# y = float(input("enter denominator:"))
# mod = x%y
# print(mod, "is the remainder of the 2 numbers")

# #exponential(**) amd floor divition(//):
# p = x**y
# fd = x//y
# print(f"{x} to the power {y} is = {p} \nfloor divition of {x} and {y} is {fd}")

# """2. math library"""
# import cmath as m #cmath for complex roots.
# a = float(input("enter the coefficient of X^2:"))
# b = float(input("enter the coefficient of X:"))
# c = float(input("enter the value of constant:"))
# dis = b**2 - 4*a*c
# root1 = (-b + m.sqrt(dis))/(2*a)
# root2 = (-b - m.sqrt(dis))/(2*a)
# print(f"{dis} is the dicriminant of the equation and \nroot of the equation are {root1} and {root2}")
# if dis > 0:
#    print(f"the roots are real and different.") 
# elif dis==0:
#     print("roots are real and equal")
# else:
#    real = -b/(2*a)
#    imaginary = m.sqrt(dis)/(2*a)
#    print(f"the roots are complex and different")

import math as m
x = float(input("enter any fractional value:"))
y = float(input("enter any fractional value:"))
print(m.ceil(x),m.floor(y)) 
#ceil rounds a number upwards to its nearest integer
#floor rounds a number downwards to its nearest integer
z = pow(x,y) #pow means x to the power y
print(z)

#area related problems:
x1 = int(input("enter the value of x1:"))
y1 = int(input("enter the value of y1:"))
x2 = int(input("enter the value of x2:"))
y2 = int(input("enter the value of y2:"))
x3 = int(input("enter the value of x3:"))
y3 = int(input("enter the value of y3:"))
ab = m.sqrt((x1-x2)**2+(y1-y2)**2)
bc = m.sqrt((x2-x3)**2+(y2-y3)**2)
ca = m.sqrt((x3-x1)**2+(y3-y1)**2)
s = (ab+bc+ca)/2
area = m.sqrt((s-ab)*(s-bc)*(s-ca)*s)
r = ab #lets assume the radius of a circle is ab.
carea = m.pi*pow(r,2)
print(f"the area of the triangle is:{area} \nthe area of the circle is:{carea}")