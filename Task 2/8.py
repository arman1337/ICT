a = int(input())
b = int(input())
c = int(input())

arr = [a, b, c]
max_ = 0
min_ = None
for i in arr:
    if i > max_:
        max_ = i
    if min_ is None:
        min_ = i
    elif i < min_:
        min_ = i
arr.remove(min_)
arr.remove(max_)
print(min_, arr[0], max_)
# arr.sort!!!!!!!!!!!!!!!!!!



