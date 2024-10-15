# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: OSCAR RODRIGUEZ (635007029)
# THANG CHAU (335000995)
# NATHANIEL ALVARENGA (735000064)
# JONATHAN BOZONE (835005736)
# Section: ENGR-102-551
# Assignment: Lab7A
# Date: 30/09/24

production = []

while True:
    try:
        widgets = int(input("Enter the number of widgets produced or enter a negative number to stop: "))
        if widgets < 0:
            break
        production.append(widgets)
    except:
        print("Please enter a valid integer.")

if len(production) > 1:
    production_length = len(production)
    for interval in range(1, production_length):
        inc = 0
        dec = 0
        total = 0
        
        for x in range(production_length - interval):
            if production[x + interval] > production[x]:
                inc += 1
            elif production[x + interval] < production[x]:
                dec += 1
            total += 1
        
        if total > 0:
            print(f"For {interval}-day intervals {(inc / total) * 100:.1f}% were increasing and {(dec / total) * 100:.1f}% were decreasing")
else:
    print("Not enough data to calculate intervals.")