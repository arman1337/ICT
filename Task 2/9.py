a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

if a1 == a2 and b1 == b2 and c1 == c2:
    print("boxes are equal")
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print("box 1 is smaller")
elif a1 >= a2 and b1 >= b2 and c1 >= c2:
    print("box 2 is smaller")
else:
    print("incomparable")