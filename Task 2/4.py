a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

a = [a1, b1, a2, b2]
for k in a:
    if k > 8 or k< 1:
        print("ERROR")

if (a2 == a1 or b2 == b1) and a2 - a1 != b2 - b1:
    print("Yes")
else:
    print("No")
