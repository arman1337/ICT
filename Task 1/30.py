kPa = float(input("kPa "))
psi = kPa / 6.89475729
mmgh = kPa * 760 / 101.325
atm = kPa / 101.325

print(psi, mmgh, atm)