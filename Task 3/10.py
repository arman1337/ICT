s = input()
case = 0
if s[0].islower() and (s[1:].isupper()):
    print(s[0].upper() + s[1:].lower())
elif s.isupper():
    print(s.lower())
elif s.islower():
    print(s.upper())
else:
    print(s)

