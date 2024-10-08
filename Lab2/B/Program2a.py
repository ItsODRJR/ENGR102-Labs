import math

print("All inputs should be in a Vector3 format without commas (x y z)")
print("Please note that none of the points can equal each other or else code will error from a divison of 0 error")

# Basically we are making the Vector3 an array
observer = [float(x) for x in input("Input the observer's position: ").split()]
p0 = [float(x) for x in input("Input the first point's position: ").split()]
p1 = [float(x) for x in input("Input the second point's position: ").split()]

p0 = [p0[i] - observer[i] for i in range(3)]
p1 = [p1[i] - observer[i] for i in range(3)]
vector1 = [x /  math.sqrt(sum([x**2 for x in p0])) for x in p0]
vector2 = [x / math.sqrt(sum([x**2 for x in p1])) for x in p1]

dot_product = sum([vector1[i] * vector2[i] for i in range(3)])

print(f"The angle between the two points as seen by the observer is {math.degrees(math.acos(dot_product))} degrees.")