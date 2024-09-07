l1 = list(input("Enter name 1: ").lower())
l2 = list(input("Enter name 2: ").lower())

for ch in l1:
    if ch in l2:
        l1.remove(ch)
        l2.remove(ch)

print(l1, l2)

c = len(l1) + len(l2)

text = list("flames")
i = 0
counter = 1

while True:
    if len(text) == 1:
        break
    if i != len(text):
        if counter == c:
            text.pop(i)
            counter = 0
            i -= 1
    else:
        i = -1
        counter -= 1
    counter += 1
    i += 1

print(text)
