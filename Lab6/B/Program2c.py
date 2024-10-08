for x in range(2, 101):
    for i in range(2, x + 1):
        if x % i == 0:
            print(f"{i} divides {x}")