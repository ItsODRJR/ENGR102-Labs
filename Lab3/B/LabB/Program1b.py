import math

normal_stress = float(input("Please input the normal stress applied to the material in MPa: "))
cohesion = float(input("Please input the cohesion of the material in MPa: "))
angle_of_friction = float(input("Please input the angle of internal friction in degrees: "))
print(f"The shear stress of the material is {cohesion + normal_stress * math.tan(math.radians(angle_of_friction))} MPa.")