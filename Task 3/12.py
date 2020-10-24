n = int(input())
s = input()
cnt = 0


def findKey(s):
    if "xxx" in s:
        return True


while findKey(s):
    pos = s.find("xxx")
    s = s.replace("xxx", "xx", 1)
    cnt += 1
print(cnt)
