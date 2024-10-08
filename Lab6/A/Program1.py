# Create the cubic polynomial on user input
coeffients = [int(x) for x in input("Enter all 4 coeffients of cubic polynimals (x x x x): ").split(" ")]

# Input lower and upper bounds
x1 = float(input("Enter the lower bound a: "))
x2 = float(input("Enter the upper bound x2: "))

tol = 1e-6

# Value of polynimal at x1 and x2
f_x1 = coeffients[0] * x1**3 + coeffients[1] * x1**2 + coeffients[2] * x1 + coeffients[3]
f_x2 = coeffients[0] * x2**3 + coeffients[1] * x2**2 + coeffients[2] * x2 + coeffients[3]

# Binary Search to get closer to the root by changing the lower and upper bounds range
if f_x1 * f_x2 > 0:
    print("No single root exists in the given interval.")
else:
    iterations = 0
    while (x2 - x1) / 2 > tol:
        iterations += 1

        # Get the midpoint between x1 and x2 and then its function value
        x_mid = (x1 + x2) / 2
        f_mid = coeffients[0] * x_mid**3 + coeffients[1] * x_mid**2 + coeffients[2] * x_mid + coeffients[3]

        if abs(f_mid) < tol: # If the function value at the midpoint is close enough to zero within the tolerance, we will break out
            break
        elif f_mid * f_x1 < 0: # If f(x_mid) and f(x1) have opposite signs, the root is between x1 and x_mid
            x2 = x_mid
            f_x2 = f_mid
        else: # If f(x_mid) and f(x1) have the same sign, the root is between x_mid and x2
            x1 = x_mid
            f_x1 = f_mid

    print(f"The root is approximately: {x_mid}")
    print(f"Found in {iterations} iterations.")