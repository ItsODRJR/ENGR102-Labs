import math

v0 = float(input("Input inital voltage: "))
v1 = float(input("Input final voltage: "))

print(f'{20 * math.log10(v1/v0)} dBV.')