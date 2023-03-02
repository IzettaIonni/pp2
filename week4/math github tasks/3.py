import math
n_sides = int(input())
s_length = float(input())
p_area = n_sides * (s_length ** 2) / (4 * math.tan(math.pi / n_sides))
print(math.floor(p_area))