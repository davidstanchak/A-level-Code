letters = input("enter 5 lowercase letters: \n")
alphabet = [chr(i) for i in range(97, 123)]

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