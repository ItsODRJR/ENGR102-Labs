def calucateStress(stress):
    if strain <= 0.01:
        return 4300 * stress
    elif strain < 0.06:
        return (20 * stress) + 42.8
    elif strain < 0.175:
        return (139.13 * stress) + 35.652
    elif strain <= 0.26:
        return ((-94.118 * stress) + 76.471)
    else:
        return "Strain exceeds fracture point."

strain = float(input("Enter strain value: "))
stress = calucateStress(strain)

try:
    print(f"The stress for the strain {strain} is {stress:0.2f} ksi")
except:
    print(stress)    
