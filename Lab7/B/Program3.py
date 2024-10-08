combos = {}
cnt = int(input("How many username and password combinations to create: "))

for x in range(cnt):
    combos[x] = {}
    combos[x][0] = input(f"Username {x + 1}: ")

for x in range(cnt):
    combos[x][1] = input(f"Password for {combos[x][0]}: ")

while True:
    username = input("Username: ")
    password = input("Password: ")

    correct = False
    for x in combos:
        combo = combos[x]
        if combo[0].lower() == username.lower() and combo[1] == password:
            print(f"Correct! Logged in as {combo[0]}")
            correct = True

    if correct:
        break
    else:
        print("Incorrect username or password. Please try again.")  