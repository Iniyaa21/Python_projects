# 1. number guessing game
import random
up = int(input("Enter upper limit: "))
low = int(input("Enter lower limit: "))
n = random.randint(low, up)
c = 0
while True:
    guess = int(input("Enter your guess: "))
    c+=1
    if guess == n:
        print("You got the answer!\nNumber of guesses:",c)
        break
    elif guess < n:
        print("Try again, you guessed too small!")
    elif guess > n:
        print("Try again, you guessed too big")
