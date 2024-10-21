count = 0

def guess_number(number):
    global count
    try:
        guess = int(input("What is your guess? "))
        count += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"You guessed it! It took you {count} guesses.")
            return True
    except:
        print("Bad input! Try again with only an integer value.")
    return False
    

def main():
    number = 27
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")
    while True:
        if guess_number(number):
            break

main()            