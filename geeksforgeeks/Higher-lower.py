import random


def rand():
    return random.randint(1, 9999)


d = {
    "Sophie Foster": rand(),
    "Ravi Singh": rand(),
    "Keefe Sencen": rand(),
    "Biana Vacker": rand(),
    "Feyre Archeron": rand(),
    "Kaz Brekker": rand(),
    "Nina Zenik": rand(),
    "Linh Cinder": rand(),
    "Scarlet Benoit": rand(),
    "Crescent Moon": rand(),
    "Winter Hayle": rand(),
    "Levana Blackburn": rand(),
    "Jacin Clay": rand(),
    "Carswell Thorne": rand(),
    "Zeev Kesley": rand(),
    "Dex Diznee": rand(),
    "Grady Ruewen": rand()
}

lst_of_keys = list(d.keys())
key1, key2 = None, None


def choose_a_key():
    return lst_of_keys[random.randint(0, len(d)-1)]


def play():
    global key1, key2
    finished = set()
    score = 0

    while True:
        if len(finished) == len(d):
            print("The end")
            break
        win = False
        if not key1:
            while True:
                key1 = choose_a_key()
                if key1 not in finished:
                    break
        if not key2:
            while True:
                key2 = choose_a_key()
                if key1 != key2 and key2 not in finished:
                    break
        finished.add(key1)
        finished.add(key2)
        print(key1, "\nVs\n", key2)
        guess = input(
            "Enter the name of the person with the highest number of followers: ")
        if d[key1] > d[key2]:
            if guess == key1:
                win = True
                key1 = None

        else:
            if guess == key2:
                win = True
                key2 = None

        if win:
            score += 1
            print(f'''----------------------------------------------------------
            Current score: {score}
--------------------------------------------------''')
        else:
            cont = input("You lost, do you wanna play again? (y/n): ")
            if cont == "n":
                break
            else:
                finished = set()
                key1 = key2 = None
                score = 0


while True:
    choice = input("Do you wanna play higher lower? (y/n): ").lower()
    if choice == "y":
        play()
    else:
        break
