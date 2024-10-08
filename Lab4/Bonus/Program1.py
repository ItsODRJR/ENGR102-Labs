velocity = float(input("Enter the velocity (m/s): "))
diameter = float(input("Enter the pipe diameter (m): "))
viscosity = float(input("Enter the kinematic viscosity (m^2/s): "))

reynolds_num = (velocity * diameter) / viscosity
    
if reynolds_num < 2300:
    flow_type = "Laminar"
elif reynolds_num > 2900:
    flow_type = "Turbulent"
else:
    flow_type = "In transition"

print(f"Reynolds Number: {reynolds_num}")
print(f"The flow is {flow_type}.")