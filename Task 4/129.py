import random

d_e = dict(zip([i for i in range(2, 13)], [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]))
n = 10000


def rollDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2


def simulation():
    d = {}
    d = d.fromkeys([i for i in range(2, 13)], 0)

    for i in range(0, n):
        total = rollDice()
        if total in d.keys():
            d[total] += 1
    return d


d = simulation()
print("Total | " + "Sim. % | " + "Exp. %")
for key in d.keys():
    print(key,  "     ", "{:.2f}".format(d[key]/n*100), "   ", d_e[key])


