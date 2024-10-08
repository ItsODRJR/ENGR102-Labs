names = str.split(input("Enter names: "), " ")
birthdates = str.split(input("Enter birthdates (DAY/MONTH/YEAR): "), " ")

print("---------------------")

for x in range(0, len(names)):
    print(names[x] + "'s birthday is on", birthdates[x])
    print("---------------------")