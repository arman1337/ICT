s = input()

d = {}

for char in s:
    if char in d.keys():
        d[char] += 1
        continue
    d[char] = 1
print(len(d))