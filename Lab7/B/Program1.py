vowels = 'aeiouy'

while True:
    word = input("Enter one word to be Pig Latinized: ").lower()

    if word:
        if word[0] in vowels:
            print(word + "yay")
        else:
            for i, v in enumerate(word):
                if v in vowels:
                    pig_latin_word = word[i:] + word[:i] + "ay"
                    print(pig_latin_word)
                    break
    else:
        print("Please enter a valid word.")

    if word == "stop": # going to put this under the code just in casse the user actually wants pig latin for the word "stop"
        print("Stopped!")
        break