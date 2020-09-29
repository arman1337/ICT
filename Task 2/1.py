arr = []

for i in range(2):
    a = int(input())
    b = int(input())
    if a > 8 or a < 1 or b > 8 or b < 1:
        print("ERROR")
    else:
        arr.append((a, b))

if arr[0][0] == arr[1][0] or arr[0][1] == arr[1][1]:
    print("YES")
else:
    print("NO")



