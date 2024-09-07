import random

d = {1: "rock", 2: "paper", 3: "scissors"}
winner = "user"

while True:
    print("""Enter choice:
    1. Rock
    2. Paper
    3. Scissors\n\n""")

    n1 = int(input("User turn: "))

    print("\nUser choice is", d[n1])
    print("\n\nIts computer turn......")

    n2 = random.randint(1, 3)

    print("\nComputer choice is", d[n2])
    print(f"\n{d[n1]} vs {d[n2]}\n")

    if (n1, n2) in [(1, 3), (2, 1), (3, 2)]:
        winner = "user"
        print(d[n1], "wins -->", winner, "wins")

    elif (n1, n2) in [(1, 2), (2, 3), (3, 1)]:
        winner = "computer"
        print(d[n2], "wins -->", winner, "wins")

    else:
        print("Tie")

    c = input("Do you want to play again? (y/n): ").lower()
    if c == "n":
        break
