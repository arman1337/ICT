import math

r = float(input("Radius "))

area = math.pi * r**2
volume = (4 * math.pi* r**3) / 3

print("Area is %.2f and volume is %.2f" % (area, volume))