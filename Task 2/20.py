n, k = [int(i) for i in input().split()]
a = []
pins = ["I"]*n
for i in range(k):
    c = [int(i) for i in input().split()]
    a.append(c)
for j in range(0, k):
    for i in range(0, n):
        if i in range(a[j][0]-1, a[j][1]):
            pins[i] = "."

for pin in pins:
    print(pin, end="")