#COMPUTER GUESSES
import random
lower = 1
upper = 1000000
while True:
    guess = random.randint(lower, upper)
    while 1:
        reply = input(
            f"Is {guess} too low or too high or correct? (l/h/c): ").lower()
        if reply in "lhc":
            break
        else:
            print("Invalid input, try again!")

    if reply == "l":
        lower = guess
    elif reply == "h":
        upper = guess
    else:
        print("Yayyyyyyyy we did it!!")
        break
