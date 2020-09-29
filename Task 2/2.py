a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a2 in range(a1-1, a1+2) and b2 in range(b1-1, b1+2):
    print("YES")
else:
    print("NO")
