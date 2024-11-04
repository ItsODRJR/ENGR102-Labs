given = open("pixel_triangle.csv")
user_input = input("Input a letter: ")

for i in given:
    string = ""
    idx = 0
    tbl = i.split(",")
    tbl[len(tbl) - 1] = tbl[len(tbl) - 1].split("\n")[0]
    for i,v in enumerate(tbl):
        for k in range(int(v)):
                string += " " if int(i) % 2 == 0 else user_input
    print(string)

given.close()