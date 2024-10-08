nums = input("Enter 3 numbers seperated by spaces (x x x): ").split(" ")

largest = nums[0]
for x in nums:
    if (x > largest):
        largest = x

print("Largest number is ", largest)