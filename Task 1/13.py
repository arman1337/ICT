a = int(input("Cents "))

penny = 1
nickel = 5
dime = 10
quarter = 25
loonie = 100
toonie = 200

while a != 0:
    if a // 200 != 0:
        print(a//200, "toonies")
        a %= 200
    if a // 100 != 0:
        print(a//100, "loonies")
        a %= 100
    if a // 25 != 0:
        print(a//25, "quarters")
        a %= 25
    if a // 10 != 0:
        print(a//10, "dimes")
        a %= 10
    if a // 5 != 0:
        print(a//5, "nickels")
        a %= 5
    if a != 0:
        print(a, "pennies")
        a = 0
