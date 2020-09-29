n = int(input())

a = [int(i) for i in input().split()]

temp = a[-1]
a.insert(0, temp)
a.pop()
for i in a:
    print(i, end=" ")