s = input()

for char in s:
    low = 0
    up = 0
    if "a" <= char <= "z":
        low += 1
    else:
        up += 1
if low >= up:
    print(s.lower())
else:
    print(s.upper())
