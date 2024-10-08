import math

i = 1
for x in range(6):
    print(f"x = {i:0.8f}, f(x) = {math.sin(i) / i:0.8f}")
    i *= 0.1