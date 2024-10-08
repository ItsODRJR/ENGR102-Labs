max = int(input("Input your max number: "))

sum = 0
for x in range(0,max + 1):
    sum += x
print("for loop output for sum:", sum)

x = 0
sum = 0
while x <= max:
    sum += x
    x += 1
print("while loop output for sum:", sum)

print("---------------------------------------------------------------")

x = 1
sum = 1
for x in range(1, max + 1):
    sum *= x
print("for loop output for product:", sum)

x = 1
sum = 1
while x <= max:
    sum *= x
    x += 1
print("while loop output for product:", sum)
