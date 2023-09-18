import random


user_lst = []
comp_lst = []
win_lst = [[0, 3, 6], [6, 7, 8], [2, 5, 8], [
    0, 1, 2], [3, 4, 5], [0, 4, 8], [2, 4, 6],[1,4,7]]
line = "______________________________________________________________________"


board = """  
 0 | 1 | 2
---|---|---
 3 | 4 | 5 
---|---|---
 6 | 7 | 8
      """
print(board)


def display():
    global board
    display = board
    for ch in board:
        if ch.isdigit():
            display = display.replace(ch, " ")
    print(display)


def win(lst):
    global win_lst, line
    if len(lst) >= 3:
        for combination in win_lst:
            strike = 0
            for ele in combination:
                if ele in lst:
                    strike += 1
                if strike == 3:
                    print(line)
                    return True


def draw():
    global board
    for ch in board:
        if ch.isdigit():
            return False
    return True


def user_turn():
    global board, user_lst, win_lst, comp_lst, user, comp
    print(f"{user}'s turn")

    while True:
        position = int(input("Input move (0-8): "))
        if position not in comp_lst + user_lst:
            break
        else:
            print("Try again")

    user_lst.append(position)
    board = board.replace(str(position), user)

    display()

    if draw():
        print("Its a draw!!!!")
        return

    if win(user_lst):
        print(f"{user} won!!")
        return
    comp_turn()


def comp_turn():
    global board, comp_lst, win_lst, comp_lst, user, comp
    print(f"{comp}'s turn")
    while True:
        position = random.randint(0, 8)
        if position not in user_lst + comp_lst:
            break
    comp_lst.append(position)
    board = board.replace(str(position), comp)

    display()

    if draw():
        print("Its a draw!!")
        return

    if win(comp_lst):
        print(f"{comp} won!!")
        return
    user_turn()


# user_turn()
first = random.choice(["user", "computer"])
if first == "user":
    print("You can go first!")
    print(line)
    user = "X"
    comp = "O"
    user_turn()

else:
    print("Computer goes first!!")
    print(line)
    user = "O"
    comp = "X"
    comp_turn()