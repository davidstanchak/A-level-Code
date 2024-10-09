letters = input("enter 5 lowercase letters: \n")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letters_array = []
for i in range(0,5):
    letters_array.append(letters[i])
    for j in range(len(alphabet)):
        if alphabet[j] == letters_array[i]:
            position = j
            print(position)
            if i == 0:
                largest = j
                smallest = j
            elif position > largest:
                largest = position
            elif position < smallest:
                smallest = position

print(alphabet[smallest]," is the smallest letter. ", alphabet[largest], " is the largest letter")