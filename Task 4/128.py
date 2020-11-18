def rLookUp(d, value):
    keys = []
    for key in d:
        if d[key] == value:
            keys.append(key)
    return keys


d = {'a': 4, 'b': 2, 'c': 3}

l = rLookUp(d, 1)

print(l)
