days = int(input("days "))
hours = int(input("hours "))
minutes = int(input("minutes "))
seconds = int(input("seconds "))

hours = hours + days * 24
minutes = minutes + hours * 60
seconds = seconds + minutes * 60

print(seconds)