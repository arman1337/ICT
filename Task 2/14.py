n = int
max_ = 0
cnt = 0
while True:
    a = int(input())
    if a == 0:
        break
    if max_ == 0:
        max_ = a
    elif a > max_:
        max_ = a
        cnt = 1
    elif a == max_:
        cnt += 1

print(cnt)
