#convert user input into moorse code
import moorse
user_sentence = input("Enter a sentence for it to be converted into moorse code: \n")
user_sentence = user_sentence.lower()
user_sentence_split = user_sentence.split()
x=0
for i in range(len(user_sentence_split)):
    eachWord = user_sentence_split[i]
    for j in range(len(eachWord)):
        letter = eachWord[j]
        x+=1
        if j == 0:
            NewLetterList = [letter]
        else:
            NewLetterList.append(letter)
    if i == 0:
        all_letters = []
        all_letters.append(NewLetterList)
    elif i > 0:
        all_letters.append(NewLetterList)

def alphabet_checker(check):
    import string  
  

    a = list(string.ascii_lowercase)
    m = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    for i in range(24):
        if a[i-1] == check:
            moorse = m[i]
            return moorse
    
for a in range(len(all_letters)): #there are "how many" arrays/words in the 2d array/sentence
    for b in range(len(all_letters[a])): #checks how many letters there are in total
        check = all_letters[a][b]
        moorse_equivilant = alphabet_checker(check)
        all_letters[a][b] = moorse_equivilant
all_letters = str(all_letters)
import re
import re

all_letters = re.sub(r"[\[\]',]|(?<=/) +|(?<=\S)/|/(?=\S)", " ", all_letters)




print(all_letters,"\n\na large gap indicates a new letter, a forward slash indicates a new word, a double backward slash indicates the end of the sentence.")