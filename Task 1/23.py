import math
s = float(input("Side"))
n = int(input("Number "))

area = n * ((s**2)/(4 * math.tan(math.pi/n)))
print(area)