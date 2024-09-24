#convert user input into moorse code

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
    if check == "a":
        moorse = "•-"
    elif check == "b":
        moorse = "-•••"
    elif check == "c":
        moorse = "-•-•"
    elif check == "d":
        moorse = "-••"
    elif check == "e":
        moorse = "•"
    elif check == "f":
        moorse = "••-•"
    elif check == "g":
        moorse = "--•"
    elif check == "h":
        moorse = "••••"
    elif check == "i":
        moorse = "••"
    elif check == "j":
        moorse = "•---"
    elif check == "k":
        moorse = "-•-"
    elif check == "l":
        moorse = "•-••"
    elif check == "m":
        moorse = "--"
    elif check == "n":
        moorse = "-•"
    elif check == "o":
        moorse = "---"
    elif check == "p":
        moorse = "•--•"
    elif check == "q":
        moorse = "--•-"
    elif check == "r":
        moorse = "•-•"
    elif check == "s":
        moorse = "•••"
    elif check == "t":
        moorse = "-"
    elif check == "u":
        moorse = "••-"
    elif check == "v":
        moorse = "•••-"
    elif check == "w":
        moorse = "•--"
    elif check == "x":
        moorse = "-••-"
    elif check == "y":
        moorse = "-•--"
    elif check == "z":
        moorse = "--••"
    return moorse
    
for a in range(len(all_letters)): #there are "how many" arrays/words in the 2d array/sentence
    for b in range(len(all_letters[a])): #checks how many letters there are in total
        check = all_letters[a][b]
        moorse_equivilant = alphabet_checker(check)
        all_letters[a][b] = moorse_equivilant
all_letters = str(all_letters)
all_letters = all_letters.replace("[","")
all_letters = all_letters.replace("]","  /")
all_letters = all_letters.replace(",","  ")
all_letters = all_letters.replace("'","")
print(all_letters)
print("a large gap indicates a new letter, a forward slash indicates a new word, a double forward slash indicated the end of the sentence. ")