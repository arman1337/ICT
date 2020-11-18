f = open("2.txt", 'r')
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = '1234567890'
alph = ['A', 'B', 'C', 'E', ['G', 'H', 'J'], ['K', 'L', 'M', 'N', 'P'], 'R', 'S', 'T', 'V', 'X', 'X', 'Y']
d = {}

for i in range(13):
    a = f.readline().replace('\n', '')
    d[a] = alph[i]

s = input()
ans = []
rural = False
if len(s) != 7\
        or s[0] in "DFIOQUWZ" \
        or s[1] not in n \
        or s[2] not in l \
        or s[4] not in n \
        or s[5] not in l \
        or s[6] not in n:
    print("Invalid postal code")
else:
    for key in d.keys():
        if len(d[key]) == 1:
            if d[key] == s[0]:
                ans.append(key)
        else:
            if s[0] in d[key]:
                ans = key
    if s[1] != '0':
        rural = True

if len(ans)>1:
    ans = " or ".join(ans)
else:
    ans = ans[0]
if rural:
    ans = " a rural address in " + ans
else:
    ans = " an urban address in " + ans
print("Postal code is for" + ans + ".")