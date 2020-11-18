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
        return True
    else:
        return False


run = True

n = 1000
ans = []
for i in range(n):
    d = card()
    cnt = 0
    while not bing(d):
        cnt += 1
        letter = a[random.randint(0, 4)]
        col = random.randint(0, 4)
        num = random.randint(1, 75)

        if d[letter][col] == num:
            d[letter][col] = 0
    ans.append(cnt)
print(ans)
print("max is ", max(ans))
print("min is ", min(ans))
print("avg is ", sum(ans) / n)
