import random


def display(d):
    for key in d.keys():
        print(key, end="   ")
    print()
    for i in range(5):
        for key in d.keys():
            print(d[key][i], end="  ")
        print()


def card():
    d = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
    j = 1
    k = 15
    for key in d.keys():
        for i in range(5):
            d[key].append(random.randint(j, k))
        j = k + 1
        k += 15
    return d


def zero_row(d):
    r = random.randint(0, 4)
    for key in d.keys():
        d[key][r] = 0
    return d


a = ['B', 'I', 'N', 'G', 'O']


def zero_col(d):
    r = random.randint(0, 4)
    for i in range(5):
        d[a[r]][i] = 0
    return d


def zero_diag(d):
    i = 0
    for key in d.keys():
        d[key][i] = 0
        i += 1
    return d


def check_row(d):
    bingo = False
    rows = [[], [], [], [], []]
    for i in range(5):
        for key in d.keys():
            rows[i].append(d[key][i])
    for row in rows:
        if row == [0, 0, 0, 0, 0]:
            bingo = True
    return bingo


def check_col(d):
    bingo = False
    cols = [[], [], [], [], []]
    c = 0;
    for key in d.keys():
        for i in range(5):
            cols[c].append(d[key][i])
        c += 1
    for col in cols:
        if col == [0, 0, 0, 0, 0]:
            bingo = True
    return bingo


def check_diag(d):
    bingo = True
    i = 0
    for key in d.keys():
        if d[key][i] != 0:
            bingo = False
        i += 1
    return bingo


def bing(d):
    if check_diag(d) or check_col(d) or check_row(d):
        print("BINGO!")
    else:
        print("NO")


d1 = card()
d2 = zero_row(card())
d3 = zero_col(card())
d4 = zero_diag(card())

bing(d1)
bing(d2)
bing(d3)
bing(d4)
