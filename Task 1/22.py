s1 = float(input("1 Side "))
s2 = float(input("2 Side "))
s3 = float(input("3 Side "))

s = (s1 + s2 + s3) / 2

area = (s * (s-s1) * (s-s2) * (s-s3)) ** (1/2)

print(area)