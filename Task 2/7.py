n = int(input())
m = int(input())
x = int(input())
y = int(input())
if n-x < x:
    x = n-x
if m - y < y:
    y = m - y

print(min(min(n-x, x), min(m-y, y)))