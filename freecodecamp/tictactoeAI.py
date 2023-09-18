import random
import copy

user_lst = []
comp_lst = []
win_lst = [[0, 3, 6],
           [6, 7, 8],
           [2, 5, 8],
           [0, 1, 2],
           [3, 4, 5],
           [0, 4, 8],
           [2, 4, 6],
           [1, 4, 7]]
line = "______________________________________________________________________"
comp_winlst_ref = copy.deepcopy(win_lst)

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
    global board, user_lst, comp_lst, user
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
    method = 2
    global board, comp_lst, user_lst, comp, comp_winlst_ref, win_lst
    print(f"{comp}'s turn")

    if not user_lst:
        position = random.randint(0, 8)
    else:

        # Looking for immediate wins  (method 0)
        for combination in win_lst:
            strike = []
            for ele in combination:
                if ele in comp_lst:
                    strike.append(ele)
            if len(strike) == 2:
                for n in combination:
                    if n not in comp_lst+user_lst:
                        position = n
                        board = board.replace(str(position), comp)
                        comp_lst.append(position)
                        display()
                        if win(comp_lst):
                            print(f"{comp} won!!")
                        return

        # looking for immediate threats (method 1)
        for combination in comp_winlst_ref:
            strike = []
            for ele in combination:
                if ele in user_lst:
                    strike.append(ele)
            if len(strike) == 2:
                for n in combination:
                    if n not in user_lst+comp_lst:
                        position = n
                        got_a_position = True
                        method = 1
                        break
                comp_winlst_ref.remove(combination)
                break
        # if no immediate threats, placing in a random position within the combination
        if method == 2:
            got_a_position = False
            for move in user_lst:
                for combination in comp_winlst_ref:
                    if move in combination:
                        for ele in combination:
                            if ele not in user_lst+comp_lst:
                                position = ele
                                comp_winlst_ref.remove(combination)
                                got_a_position = True
                                break
                    if got_a_position:
                        break
                if got_a_position:
                    break
        if not got_a_position:
            while True:
                position = random.randint(0, 8)
                if position not in comp_lst + user_lst:
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
