# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: OSCAR RODRIGUEZ (635007029)
# THANG CHAU (335000995)
# NATHANIEL ALVARENGA (735000064)
# JONATHAN BOZONE (835005736)
# Section: ENGR-102-551
# Assignment: Lab9A
# Date: 14/10/24

def get_points():
    points = []
    print("Enter data points as x, y pairs. Type 'done' when finished.")
    
    while True:
        input = input("Enter x y: ").strip().lower()
        if input == 'done':
            break
        try:
            x, y = input.split()
            points.append((float(x), float(y)))
        except ValueError:
            print("Invalid input. Please enter x, y as just \"x y\".")
    
    return sorted(points)

def interpolate(x, x0, y0, x1, y1):
    return y0 + (y1 - y0) * ((x - x0) / (x1 - x0))

def get_y_value(points, query_x):
    x_values, y_values = zip(*points)
    
    if query_x <= x_values[0]:
        return interpolate(query_x, x_values[0], y_values[0], x_values[1], y_values[1])
    elif query_x >= x_values[-1]:
        return interpolate(query_x, x_values[-2], y_values[-2], x_values[-1], y_values[-1])
    
    for i in range(1, len(points)):
        if query_x < x_values[i]:
            return interpolate(query_x, x_values[i-1], y_values[i-1], x_values[i], y_values[i])
    
    return None

data_points = get_points()

if len(data_points) < 2:
    print("At least two data points are required.")
else:
    while True:
        query_x = input("Enter an x value to query, or type 'exit' to quit: ")
        if query_x == 'exit':
            break
        try:
            query_x = float(query_x)
            result_y = get_y_value(data_points, query_x)
            print(f"Estimated y value for x = {query_x}: {result_y}")
        except:
            print("Invalid input. Please enter a valid x value.")  