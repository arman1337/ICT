import math

t1, g1 = input("First point ").split()
t2, g2 = input("Second point ").split()

t1, g1 = math.radians(float(t1)), math.radians(float(g1))
t2, g2 = math.radians(float(t2)), math.radians(float(g2))

distance = 6371.01 * math.acos((math.sin(t1)*math.sin(t2))+(math.cos(t1)*math.cos(t2)*math.cos(g1-g2)))

print(round(distance, 2))