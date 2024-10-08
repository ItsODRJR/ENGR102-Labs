import math

vectorA = [int(x) for x in input("Enter another 2D or 3D vector (x x) / (x x x): ").split()]  
if len(vectorA) == 3:
    vectorB = [int(x) for x in input("Enter another 3D vector (x x x: ").split()]  
elif len(vectorA):
    vectorB = [int(x) for x in input("Enter another 2D vector (x x): ").split()]     
else:
    print("Error creation first vector. Please try again.")    

if len(vectorA) == len(vectorB):
    print(f"Magnitude of A: {math.sqrt((vectorA[0] * vectorA[0]) + (vectorA[1] * vectorA[1]) + (vectorA[2] * vectorA[2] if len(vectorA) == 3 else 0))}")
    print(f"Magnitude of B: {math.sqrt((vectorB[0] * vectorB[0]) + (vectorB[1] * vectorB[1]) + (vectorB[2] * vectorB[2] if len(vectorA) == 3 else 0))}")
    print(f"A + B: ({vectorA[0] + vectorB[0]}, {vectorA[1] + vectorB[1]}{', ' + vectorA[2] + vectorB[2] if len(vectorA) == 3 else ''})")
    print(f"A - B: ({vectorA[0] - vectorB[0]}, {vectorA[1] - vectorB[1]}{', ' + vectorA[2] - vectorB[2] if len(vectorA) == 3 else ''})")
    print(f"Dot Product of A and B: {(vectorA[0] * vectorB[0]) + (vectorA[1] * vectorB[1]) + (vectorA[2] * vectorB[2] if len(vectorA) == 3 else 0)}")