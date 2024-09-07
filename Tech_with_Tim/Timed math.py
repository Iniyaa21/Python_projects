import time
import random
operators = ["+", "-", "*"]

input("Press enter to start! ")
print("______________________________________________________\n")
current_time = time.time()
for i in range(1, 11):
    n1, n2 = random.randint(1, 12), random.randint(1, 12)
    op = operators[random.randint(0, len(operators)-1)]
    if op == "+":
        answer = n1 + n2
    elif op == "-":
        answer = n1 - n2
    else:
        answer = n1 * n2
    while True:
        user_answer = int(input(f"Problem #{i}: {n1} {op} {n2} = "))
        if user_answer == answer:
            break
        else:
            print("Try again!")
new_time = time.time()
duration = new_time - current_time
print("______________________________________________________")
print(f"Nice work! You finished in {duration} seconds!")
