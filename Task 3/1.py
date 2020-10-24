s = input().lower()
f_s = ""
vowels = ["a", "e", "i", "o", "u", "y"]
for char in s:
    if char not in vowels:
        f_s += "."+char

print(f_s)