d = {1: ["A", 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
     2: ['D', 'G'],
     3: ['B', 'C', 'M', 'P'],
     4: ['F', 'H', 'V', 'W', 'Y'],
     5: ['K'],
     8: ['J', 'X'],
     10: ['Q', 'Z']}

s = input()

total = 0

for char in s:
    for key in d.keys():
        if char in d[key]:
            total += key

print(total)