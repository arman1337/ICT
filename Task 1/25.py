ss = int(input("Seconds "))
D = 0
HH = 0
MM = 0

minutes = 60
hours = 3600
days = 24 * 3600

if ss // days != 0:
    D = ss // days
    ss %= days
if ss // hours != 0:
    HH = ss // hours
    ss %= hours
if ss // minutes != 0:
    MM = ss // minutes
    ss %= minutes
print("%i:%02i:%02i:%02i" % (D, HH, MM, ss))