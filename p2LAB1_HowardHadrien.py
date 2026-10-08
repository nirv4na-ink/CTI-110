'''
Hadrien Howard
9/24/26
use math library to calculate circle features
'''
import math

#get radius from user as a float
radius = float(input("enter the radius as a float"))

print()

#calculate Diameter

Diameter = 2 * radius
print(f"The diameter of the circle is: {Diameter:.1f}")

print()

#calculate circumference
circumference = 2 * math.pi * radius

# display circumference
print(f"The circumference of the circle is: {circumference:.2f}")

# calculate the area
area = math.pi * math.pow(radius, 2)

print(f"The area of the circle is: {area:.3f}")