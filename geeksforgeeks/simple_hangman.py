# 2.hangman project
import random
lst = ["keefe", "sophie", "biana", "dex", "fitz", "tam", "grady", "edaline", "linh", "romhilda"]
word = lst[random.randint(0,(len(lst) - 1))]
dashes = ""
def remove_spaces(str):
    s = ""
    for ch in str:
        if ch.isalpha():
            s+=ch
    return s
    
def find_index(letter, word):
    indlst = []
    if word.count(letter) > 1:
        #there are multiple occurrences
        for i in range(len(word)):
            if word[i] == letter:
                indlst.append(i)
    else:
        indlst.append( word.index(letter))
    for i in range(len(indlst)):
        indlst[i] *= 2
    return indlst
            
for i in range(len(word)):
    dashes+="_ "
print(dashes)
    
while True:
    if remove_spaces(dashes) == word:
        print("Congrats, you got it!")
        break
    letter = input("Guess a letter: ").lower()
    if letter in word:
        ind = find_index(letter, word)
        d = ""
        for i in range(len(dashes)):
            if i in ind:
                d+=letter
            else:
                d+=dashes[i]
        print(d)
        dashes = d
        
    else:
        print("Try again")
