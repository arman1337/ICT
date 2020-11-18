def init_d():
    alph = "abcdefghijklmnopqrstuvwxyz"
    d = {1: ['.', ',', '?', '!', ':']}
    k = 2
    for i in range(0, len(alph) - 2, 3):
        if alph[i] == 's':
            d[k - 1].append(alph[i])
            d[k] = [alph[i + 1], alph[i + 2], alph[i + 3]]
            k += 1
            continue
        elif alph[i] == 'v':
            d[k] = [alph[i + 1], alph[i + 2], alph[i + 3], alph[i + 4]]
        else:
            d[k] = [alph[i], alph[i + 1], alph[i + 2]]
        k += 1
    d[0] = " "
    return d


decode = init_d()

s = input().lower()
text = []

for letter in s:
    for key in decode.keys():
        for i in range(len(decode[key])):
            if decode[key][i] == letter:
                text.append([key, i + 1])

for a in text:
    for i in range(a[1]):
        print(a[0], end="")
    print(end=" ")
