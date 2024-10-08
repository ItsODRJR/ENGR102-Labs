name = input("Enter a person's name: ")
city = input("Enter the name of a city: ")
color = input("Enter your favorite color: ")
activity = input("Enter a word ending in '-ing': ")
age = int(input("Enter your age: "))
birthdayMonth = input("Enter a birthday month: ")

print(f"\n\tOnce upon a time, there was a person named {name}.\n" \
        f"{name} lived in the epic city of {city}, where the lake water was {color}.\n" \
        f"Last week, {name} decided to go {activity} in the lake.\n" \
        f"At only {age} years old (born in {birthdayMonth}!), {name} was known for being the best at {activity}.\n" \
        f"Legend has it, \"{name} is the champion of {activity} in {city}!\"\n" \
        f"Now, {name}'s legacy was continued with stories known for being the \'{activity}\' champion of {city}.")
