day = int(input("Enter the day number (1-100): "))
    
if day < 1 or day > 100:
    print("Invalid day. Please enter a number between 1 and 100.")
else:
    if day <= 10:
        total_widgets = day * 10
    elif day <= 60:
        total_widgets = 100 + (day - 10) * 40
    elif day <= 100:
        total_widgets = 2100 + sum((40 - x) for x in range(1, day - 59))
        
    print(f"Day entered: {day}")
    print(f"Total widgets produced up to day {day}: {total_widgets}")