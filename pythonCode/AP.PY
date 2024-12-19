won = False
turn = 1
last = 0

while not won:
    if turn % 2 == 0:
        currentPlayer = "2"
    else:
        currentPlayer = "1"
        
    choice = input(f"{currentPlayer}, enter a choice.").split(",")
    for i in range(choice):
        
        numbers.append(current)






