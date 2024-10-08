count = 0
total = 0
max = float('-inf')
min = float('inf')

while True:
    measurement = float(input("Enter a measurement or a negative number to stop: "))
    if measurement < 0:
        break
    
    count += 1
    total += measurement

    if measurement > max:
        max = measurement

    if measurement < min:
        min = measurement

if count > 0:
    print(f"Average: {total / count}")
    print(f"Maximum: {max}")
    print(f"Minimum: {min}")
else:
    print("No valid measurements entered.")