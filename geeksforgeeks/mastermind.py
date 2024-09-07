import random

n = random.randint(1000,9999)
n = str(n)
#print(n)
tries = 0
while True:
    t = input("Guess the 4 digit number: ")
    tries+=1
    print()

    c = 0
    lst = []

    for i in range(4):
        if n[i] == t[i]:
            c+=1
            lst.append(i)
    if n == t:
        print("Congrats, you have won!")
        print("\nYou took", tries, "tries!")
        break

    elif c == 0:
        print("Not quite the number, try again!\n")
        continue
    else:
        if c == 1:
            print("Not quite the number, but you got", c, "digit in the right position")
        else:
            print("Not quite the number, but you got", c, "digits in the right position")

        for i in range(4):
            if i not in lst:
                print("X", end =" ")
            else:
                print(n[i], end=" ")
        print("\n")
