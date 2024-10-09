from math import *
#Part 1: Identifying floating-point problems
a = 1/7
print(a)
b = a*7
print(b)

print("--------------------")

a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)

print("--------------------")

x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)

print("--------------------")

large = 1.0e16
small = 1.0e-16
sum1 = (large + small) - large
sum2 = small
print(f"Is (large + small) - large the same as small? {sum1 == sum2}")

print("--------------------")

A = 1.000000000000001
B = 1.000000000000000
sum1 = A - B
sum2 = (A - B) + 1e-16 - 1e-16
print(f"Is (A - B) the same as ((A - B) + 1e-16 - 1e-16)? {sum1 == sum2}")

print("--------------------")

small_number = 1.0e-16
iterations = 1_000_000
sum1 = sum(small_number for _ in range(iterations))
sum2= iterations * small_number
print(f"Is the sum of {iterations} small_number the same as iterations * small_number? {sum1 == sum2}")
error = abs(sum1 - sum2)
print(f"Difference between the two results: {error}")
print("--------------------")

#Part 2: Tolerances for Comparisons

tolerance_count = 1e-10

a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)

if abs(b-e) < tolerance_count:
    print("b and e are equal within tolerance of", tolerance_count)
else:
    print("b and e are NOT equal within tolerance of",tolerance_count)

print("--------------------")

tolerance_count = 1e-7
x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)
if abs(y-z) < tolerance_count:
    print("y and z are equal within tolerance of", tolerance_count)
else:
    print("y and z are NOT equal within tolerance of", tolerance_count)