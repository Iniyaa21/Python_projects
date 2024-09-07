import random
from new import style
import time

no_of_players = int(input("Enter the number of players (2-4): "))
scores = [0 for i in range(no_of_players)]
winner = 0


def roll():
    n = random.randint(1, 6)
    style(n)
    return n


while max(scores) < 100:
    i = 1
    for player in scores:
        if winner:
            break
        print("\n\n\n\n\n")
        time.sleep(1)
        print("_______________________________________________")
        print(f"PLAYER {i}'S TURN")
        print(f"PLAYER {i}'S CURRENT SCORE ---> {scores[i-1]}")
        print("_______________________________________________")
        temp_score = 0
        while 1:
            n = roll()
            if n == 1:
                print("\n\nYou rolled a one, end of turn!")
                time.sleep(2)
                print("_______________________________________________")
                print(f"YOUR CURRENT SCORE ----> {scores[i-1]}")
                print("_______________________________________________")
                break
            else:
                temp_score += n
                choice = input(
                    "\nDo you want to continue? (y/n): ").lower()
                if choice == "n":
                    scores[i-1] += temp_score
                    print("_______________________________________________")
                    print(
                        f"YOUR CURRENT SCORE ----> {scores[i-1]}")
                    print("_______________________________________________")
                    if scores[i-1] >= 100:
                        winner = i
                        break
                    break

        i += 1
print(f"\n\nPLAYER {winner} won!!!!!")
