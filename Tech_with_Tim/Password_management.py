# password management system

import csv
file_path = r"C:\Users\kavit\OneDrive\Desktop\Coding\Files\passwords.csv"


def series(length):
    lst = ["14"]
    for i in range(1, length):
        lst.append(str(int(lst[i-1]) + int(11*i)))
    actual_lst = []
    for ele in lst:
        actual_lst.append(ele[0])
    return actual_lst


def encryptor(password):
    new = ""
    length = len(password.strip())
    key = series(length)
    # print(key)
    index = 0
    for jump in key:
        asc = ord(password[index])
        asc += int(jump)
        new += chr(asc)
        index += 1
    return new


def decryptor(password):
    key = series(len(password))
    old, index = "", 0
    for jump in key:
        asc = ord(password[index])
        asc -= int(jump)
        old += chr(asc)
        index += 1
    return old


def add(user, password):
    f = open(file_path, "a", newline="")
    wob = csv.writer(f)
    wob.writerow([user, encryptor(password)])
    print("\nRecord added successfully")
    f.close()


def get(user):
    f = open(file_path, newline="")
    found = False
    rob = csv.reader(f)
    for row in rob:
        if row:
            if row[0] == user:
                decrypted = decryptor(row[1])
                print(f"The required password is {decrypted}")
                found = True
    if not found:
        print("Record not found")
    f.close()


def modify(user, new):
    f = open(file_path, "r", newline="")
    lst_of_rows = []
    rob = csv.reader(f)
    found = False
    for row in rob:
        if row:
            if row[0] == user:
                row[1] = encryptor(new)
                found = True
            lst_of_rows.append(row)
    if not found:
        print("Record not found")
    else:
        f = open(file_path, "w", newline="")
        wob = csv.writer(f)
        wob.writerows(lst_of_rows)
        f.close()


while True:
    print("""PASSWORD MANAGEMENT SYSTEM
1. Add new password
2. Modify existing password
3. Fetch existing password)
4. Exit""")

    ch = int(input("Enter your choice (1-3): "))
    if ch == 1:
        user = input("Enter username: ")
        password = input("Enter password: ")
        add(user, password)

    elif ch == 2:
        user = input("Enter username to search: ")
        new = input("Enter new password: ")
        modify(user, new)

    elif ch == 3:
        user = input("Enter the username to search: ")
        get(user)

    elif ch == 4:
        break

    else:
        print("Invalid choice, try again..")
