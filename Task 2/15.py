a = [0, 1]
for i in range(2, 100):
    b = a[i-2] + a[i-1]
    a.append(b)

n = int(input())
if n in a:
    print(a.index(n))
else:
    print(-1)