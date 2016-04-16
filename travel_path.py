from itertools import permutations
import math

min_distance = math.inf
min_path = []

delivery_coords = []
delivery_coords.append((2.307,-.77))
delivery_coords.append((.251,4.23))
delivery_coords.append((2.305,-.963))
delivery_coords.append((-3.00,-3.0149))
delivery_coords.append((3.32,2.13))


for item in permutations(delivery_coords):
    total_distance = 0
    x1 = 0
    y1 = 0
    for house in range(0, len(item)):
        x2 = item[house][0]
        y2 = item[house][1]

        d = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        total_distance += d

        x1 = x2
        y1 = y2

    if total_distance < min_distance:
        min_distance = total_distance
        min_path = item

print(min_path)