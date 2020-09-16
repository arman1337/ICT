p = float(input("Pressure "))
v = float(input("Volume "))
t = float(input("Temperature ")) + 273.15
R = 8.314

n = (p*v) / (R*t)

print(n)