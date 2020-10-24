n = int(input())
s = input()
f = ""
zero = "zero"
one = "one"


def checkZero():
    for char in zero:
        if char not in s:
            return False
    return True


def checkOne():
    for char in one:
        if char not in s:
            return False
    return True


def delZero(s):
    temp = s
    for char in zero:
        temp = temp.replace(char, "", 1)
    return temp


def delOne(s):
    temp = s
    for char in one:
        temp = temp.replace(char, "", 1)
    return temp


while checkOne():
    f += "1"
    s = delOne(s)

while checkZero():
    f += "0"
    s = delZero(s)
print(" ".join(f))
