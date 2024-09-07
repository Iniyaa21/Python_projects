import random
from new import style
import time

global user_score, comp_score, winner
user_score = 0
comp_score = 0
winner = 0


def roll():
    n = random.randint(1, 6)
    style(n)
    return n


def user_turn():
    global user_score, comp_score, winner
    if winner:
        print(f"{winner} won!!!!!")
    else:
        temp_score = 0
        while 1:
            n = roll()
            if n == 1:
                print("\n\nYou rolled a one, end of turn!")
                print("_______________________________________________")
                print(f"\n\nYOUR CURRENT SCORE ----> {user_score}\n\n")
                print("_______________________________________________")
                break
            else:

                temp_score += n
            choice = input("\nDo you want to continue? (y/n): ").lower()
            if choice == "n":
                user_score += temp_score
                print("_______________________________________________")
                print(f"\n\nYOUR CURRENT SCORE ----> {user_score}\n\n")
                print("_______________________________________________")
                if user_score >= 100:
                    winner = "You"
                break
        comp_turn()


def comp_turn():
    global user_score, comp_score, winner
    if winner:
        print(f"{winner} won!!!!")
    else:
        temp_score = 0
        number_of_turns = random.randint(1, 10)
        for i in range(number_of_turns):
            n = roll()
            time.sleep(1)
            if n == 1:
                print("\n\n Computer rolled a one, end of turn!")
                print("_______________________________________________")
                print(f"\n\nCOMPUTER'S CURRENT SCORE ----> {comp_score}\n\n")
                print("_______________________________________________")
                break
            else:
                temp_score += n
        else:
            comp_score += temp_score
            print("_______________________________________________")
            print(f"\n\nCOMPUTER'S CURRENT SCORE ----> {comp_score}\n\n")
            print("_______________________________________________")
            if comp_score >= 100:
                winner = "Computer"
        user_turn()


user_first = random.randint(0, 1)
if user_first:
    print("\nIts your turn!!\n")
    user_turn()

else:
    print("Its the computer's turn!!\n")
    comp_turn()
