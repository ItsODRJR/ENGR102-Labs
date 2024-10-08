import math

stringNums = input("Enter 3 coefficients for your quadratic equation seperated by spaces (x x x): ").split(" ")
nums = [int(x) for x in stringNums]

if (nums[0] == 0):
    if (nums[1] == 0):
        if (nums[2] == 0):
            print("Inputted all 0. Infinitly many roots. Not very useful though.")
        else:
            print("No solution exists as this would just be a horizontal line at y = ", nums[2])
    else:
        root = -nums[2] / nums[1]
        print(f"The only root is x = {root} as this is a linear equation.")
else:
    discriminant = nums[1] ** 2 - 4 * nums[0]*nums[2]
        
    if (discriminant > 0):
        root0 = (-nums[1] + math.sqrt(discriminant)) / (2 * nums[0])
        root1 = (-nums[1] - math.sqrt(discriminant)) / (2 * nums[0])
        print(f"This equation has two real distinct roots: x = {root0} and x = {root1}")
    elif (discriminant == 0):
        root = -nums[1] / (2 * nums[0])
        print(f"This equation has one real roots: x = {root}")
    else:
        real = -nums[1] / (2 * nums[0])
        fake = math.sqrt(-discriminant) / (2 * nums[0])
        print(f"This equation has two complex roots: x = {real} + {fake}i and x = {real} - {fake}i")
