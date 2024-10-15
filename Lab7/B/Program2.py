import math

vectorA = [int(x) for x in input("Enter a vector (x1 x2 x3 ...): ").split()]
vectorB = [int(x) for x in input(f"Enter another vector of the same dimension ({len(vectorA)}D): ").split()]

if len(vectorA) != len(vectorB):
    print("Error: Vectors must be of the same dimension.")
else:
    print(f"Magnitude of A: {math.sqrt(sum([vectorA[i] ** 2 for i in range(len(vectorA))]))}")
    print(f"Magnitude of B: {math.sqrt(sum([vectorB[i] ** 2 for i in range(len(vectorB))]))}")
    print(f"A + B: {[vectorA[i] + vectorB[i] for i in range(len(vectorA))]}")
    print(f"A - B: {[vectorA[i] - vectorB[i] for i in range(len(vectorA))]}")
    print(f"Dot Product of A and B: {sum([vectorA[i] * vectorB[i] for i in range(len(vectorA))])}")
