import random


def rand():
    while True:
        n = str(random.randint(1000, 9999))
        if len(set(n)) == len(list(n)):
            return n


def user_guess():
    global input_message, guess
    while True:
        guess = input(input_message)

        if len(list(guess)) != 4:
            input_message = "Kindly enter a 4 digit number: "
            continue

        if len(set(guess)) != len(list(guess)):
            input_message = "You have entered duplicate digits. Try again: "
            continue

        else:
            input_message = "Enter a 4 digit number (with no duplicate digits): "
            break


n = rand()
input_message = "Enter a 4 digit number (with no duplicate digits): "
user_guess()


while True:
    bulls = cows = 0
    i = 0
    bulls_lst = []

    for ch in n:
        if ch == guess[i]:
            bulls += 1
            bulls_lst.append(ch)
        i += 1

    for ch in guess:
        if ch not in bulls_lst:
            if ch in n:
                cows += 1

    if bulls == 4:
        print("You won!")
        break

    else:
        print(f"Bulls: {bulls}\nCows: {cows}")
        user_guess()
