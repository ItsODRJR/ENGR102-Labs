import math

# Analytical derivative of user created polynomial
print("First, lets evaluate a polynomial using it's derivative")
coefficients = [int(x) for x in input("Input the 4 coefficients of your cubic polynomical function (x x x x): ").split(" ")]
print(f"f'(x) = {str(coefficients[0] * 3)}x^2 + {str(coefficients[1] * 2)}x + {coefficients[2]}")
x = float(input("Input the value of x you want to plug into f'(x): "))

# Numerical derivative of user created polynomial
deltaX = 0.1
estimate_limit = 1e-6
derivative_estimate = 0
i = 0

while True:
    fx = coefficients[0] * x**3 + coefficients[1] * x**2 + coefficients[2] * x + coefficients[3]
    fx_delta = coefficients[0] * (x + deltaX)**3 + coefficients[1] * (x + deltaX)**2 + coefficients[2] * (x + deltaX) + coefficients[3]
    numerical_derivative = (fx_delta - fx) / deltaX

    if abs(numerical_derivative - derivative_estimate) < estimate_limit:
        break
    
    derivative_estimate = numerical_derivative
    deltaX /= 2
    i += 1

print(f"Analytical derivative at x = {x}: {((coefficients[0] * 3) * (x**2)) + ((coefficients[1] * 2) * x) + coefficients[2]}")
print(f"Numerical derivative at x = {x}: {numerical_derivative}")
print(f"Iterations required: {i}")

print("---------------------------------------------------------------------------------------")

print(f"We are going to use a more complex function now, f(x) = sin(x) + cos(x)")
x_val = float(input("Input the value of x you want to evaluate the complex function at (in radians): "))

# Numerical derivative of user sin(x) + cos(x)
deltaX = 0.1
estimate_limit = 1e-6
derivative_estimate = 0
i = 0

while True:
    fx_complex = math.sin(x_val) + math.cos(x_val)
    fx_delta_complex = math.sin(x_val + deltaX) + math.cos(x_val + deltaX)
    
    numerical_derivative = (fx_delta_complex - fx_complex) / deltaX

    if abs(numerical_derivative - derivative_estimate) < estimate_limit:
        break
    
    derivative_estimate = numerical_derivative
    deltaX /= 2
    i += 1

print(f"Numerical derivative of the complex at x = {x_val}: {numerical_derivative}")
print(f"Iterations required: {i}")

print(f"Now, f(x) = tan(x) + e^x")
x_val = float(input("Input the value of x you want to evaluate the complex function at (in radians): "))

# Numerical derivative of user tan(x) + e^x
deltaX = 0.1
estimate_limit = 1e-6
derivative_estimate = 0
i = 0

while True:
    fx_complex = math.tan(x_val) + math.exp(x_val)
    fx_delta_complex = math.tan(x_val + deltaX) + math.exp(x_val + deltaX)
    
    numerical_derivative = (fx_delta_complex - fx_complex) / deltaX

    if abs(numerical_derivative - derivative_estimate) < estimate_limit:
        break
    
    derivative_estimate = numerical_derivative
    deltaX /= 2
    i += 1

print(f"Numerical derivative of the complex at x = {x_val}: {numerical_derivative}")
print(f"Iterations required: {i}")

print(f"Now, f(x) = cos(x) + log10x")
x_val = float(input("Input the value of x you want to evaluate the complex function at (in radians): "))

# Numerical derivative of user cos(x) + log10x
deltaX = 0.1
estimate_limit = 1e-6
derivative_estimate = 0
i = 0

while True:
    fx_complex = math.cos(x_val) + math.log10(x_val)
    fx_delta_complex = math.cos(x_val + deltaX) + math.log10(x_val + deltaX)
    
    numerical_derivative = (fx_delta_complex - fx_complex) / deltaX

    if abs(numerical_derivative - derivative_estimate) < estimate_limit:
        break
    
    derivative_estimate = numerical_derivative
    deltaX /= 2
    i += 1

print(f"Numerical derivative of the complex at x = {x_val}: {numerical_derivative}")
print(f"Iterations required: {i}")

# Numerical derivative of user cos(x) / sin(x), or I guesss cot(x)
print(f"Now, f(x) = cos(x) / sin(x)")
x_val = float(input("Input the value of x you want to evaluate the complex function at (in radians): "))

deltaX = 0.1
estimate_limit = 1e-6
derivative_estimate = 0
i = 0

while True:
    fx_complex = math.cos(x_val) / math.sin(x_val)
    fx_delta_complex = math.cos(x_val + deltaX) / math.sin(x_val + deltaX)
    
    numerical_derivative = (fx_delta_complex - fx_complex) / deltaX

    if abs(numerical_derivative - derivative_estimate) < estimate_limit:
        break
    
    derivative_estimate = numerical_derivative
    deltaX /= 2
    i += 1

print(f"Numerical derivative of the complex at x = {x_val}: {numerical_derivative}")
print(f"Iterations required: {i}")