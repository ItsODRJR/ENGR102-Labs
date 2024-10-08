x = 2
total_prime = 0
while x <= 100:
    prime = "\b"
    total_prime += 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            prime = "not"
            total_prime -= 1
            break
    print(f"{x} is {prime} prime")
    x += 1
print(f"There are {total_prime} prime numbers between 2 and 100")