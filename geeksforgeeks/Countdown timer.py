import time
import os

t = int(input("Enter the time in seconds: "))


def display(t):
    mins = t//60
    seconds = t % 60
    if len(str(mins)) == 1:
        mins = f"0{mins}"
    if len(str(seconds)) == 1:
        seconds = f"0{seconds}"

    print(f"{mins}:{seconds}")


def clearscreen():
    os.system('cls')


while t:
    display(t)
    time.sleep(1)
    t -= 1
    clearscreen()
print("FIRE IN THE HOLE")
