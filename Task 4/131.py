f = open("1.txt", 'r')

d = {}

for i in range(36):
    a, b = f.readline().split()
    d[a] = b

s = input().upper()

for char in s:
    if char in d.keys():
        print(d[char], end=" ")
    else:
        continue
