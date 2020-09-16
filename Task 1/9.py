a = float(input("If you put "))
print("You will get ")

for x in range(1, 4):
    print("For the", x, "year", round(a * (1.04**x), 2))