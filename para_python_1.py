from math import *

#2 Вариант

alpha = int(input("Enter the angle in radians: "))
z1 = cos(alpha) + sin(alpha) + cos(3 * alpha) + sin(3 * alpha)
z2 = 2 * (2 ** 0.5) * cos(alpha) * sin((pi / 4) + 2 * alpha)
print(z1, z2)