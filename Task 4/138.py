import random


def display():
    for key in d.keys():
        print(key, end="   ")
    print()
    for i in range(5):
        for key in d.keys():
            print(d[key][i], end="  ")
        print()


d = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}

j = 1
k = 15
for key in d.keys():
    for i in range(5):
        d[key].append(random.randint(j, k))
    j = k + 1
    k += 15
display()
