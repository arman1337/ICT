T = float(input("Temp "))
V = float(input("Speed "))

if T > 10 or V < 4.8:
    print("Index is invalid")
else:
    print(int(13.12 + 0.6215 * T - 11.37 * V ** 0.16 + 0.3965 * T * V ** 0.16))
