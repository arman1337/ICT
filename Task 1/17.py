heat_cap = 4.186
jToKWH = 2.777 * 10**-7

volume = float(input("Volume "))
temp = float(input("Temperature "))
price = float(input("Cost "))

energy = volume * temp * heat_cap
kwh = energy * jToKWH
cost = kwh * price

print("Energy needed is %.2f which will cost %.2f" % (energy, cost))