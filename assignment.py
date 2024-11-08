#Write a python program to calculate the Area 
# of a circle. Getting the radius as an input from the user

import math

radius = float(input("Enter the radius of the circle : "))

area = math.pi * (radius ** 2)

print("Area is", area)


#write a python program to calculate the hypotenuse 
# of a right angle triangle using the pythagoras formula 
# a2+b2=c2. where c is the hypotenuse. "a" and "b" are both input from the user. 

a = float(input("Enter the value of a :"))
b = float(input("Enter the value of b :"))

c = math.sqrt(a **2 + b **2)

print("The hypotenuse of the right angle triangle is :", c)