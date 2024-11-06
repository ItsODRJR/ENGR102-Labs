user_csv_input = input("Input the filename: ")
given = open(user_csv_input)
user_input = input("Input a letter: ")
lines = []

for i in given:
    string = ""
    idx = 0
    tbl = i.split(",")
    tbl[len(tbl) - 1] = tbl[len(tbl) - 1].split("\n")[0]
    for i,v in enumerate(tbl):
        for k in range(int(v)):
                string += " " if int(i) % 2 == 0 else user_input
    lines.append(string)
    
with open(user_csv_input.split(".")[0] + ".txt", 'w') as art_file:
        for i,v in enumerate(lines):
              art_file.write(v + "\n")

given.close()
