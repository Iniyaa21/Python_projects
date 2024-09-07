import random

choice = int(input("Enter 1 if you wanna go first and 2 if you wanna go second: "))
lst = []
c = 0
if choice == 1:
    while True:
        n = int(input("How many numbers do u wanna enter? "))
        lst1 = eval(input("Enter the list of numbers: "))
        # checking to see if the elements are sequential
        if lst1[0] != (c + 1):
            print("Enter numbers sequentially, try again")
            print(lst)
            continue
        for i in range(len(lst1)):
            try:
                if (lst1[i] + 1) != lst1[i + 1]:
                    print("Enter numbers sequentially, try again")
                    print(lst)
                    break
            except IndexError:
                break
        else:
            lst1.clear()
        if lst1 != []:
            if 21 in lst1:
                print("You lost!")
                break
            else:
                lst.extend(lst1)
                print(lst)
                c+=n
                lst2 = []
                n_ = random.randint(1,4)
                for i in range(n_):
                    c+=1
                    lst2.append(c)
                if 21 in lst2:
                    print("You won!")
                    break
                else:
                    lst.extend(lst2)
                    print(lst)

elif choice == 2:
    x = 1
    while True:
        if x == 1:
            lst2 = []
            n_ = random.randint(1, 4)
            for i in range(n_):
                c += 1
                lst2.append(c)
            if 21 in lst2:
                print("You won!")
                break
            else:
                lst.extend(lst2)
                print(lst)
        n = int(input("How many numbers do u wanna enter? "))
        lst1 = eval(input("Enter the list of numbers: "))
        # checking to see if the elements are sequential
        if lst1[0] != (c + 1):
            print("Enter numbers sequentially, try again")
            print(lst)
            x = 0
            continue
        for i in range(len(lst1)):
            try:
                if (lst1[i] + 1) != lst1[i + 1]:
                    print("Enter numbers sequentially, try again")
                    print(lst)
                    break
                    x = 0
            except IndexError:
                break
        else:
            lst1.clear()
        if lst1 != []:
            if 21 in lst1:
                print("You lost!")
                break
            else:
                lst.extend(lst1)
                print(lst)
                x = 1
                c += n
