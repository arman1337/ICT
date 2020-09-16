a, b = input("Feet and inches ").split()
print(round((int(a) * 12 + int(b)) * 2.54, 2), "cm")
