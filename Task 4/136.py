alph = "abcdefghijklmnopqrstuvwxyz"

def make_d(s):
    d = {}
    for char in s:
        if char in alph:
            if char in d.keys():
                d[char] += 1
                continue
            d[char] = 1
    return d


s1 = input().lower()
s2 = input().lower()

d1 = make_d(s1)
d2 = make_d(s2)

k1 = (d1.keys())
k2 = (d2.keys())

v1 = [i for i in d1.values()]
v2 = [i for i in d2.values()]

if k1 == k2 and v1.sort() == v2.sort():
    print("Yes")
else:
    print("No")

