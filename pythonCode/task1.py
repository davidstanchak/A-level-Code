valid = False
while valid == False:
    bags = int(input("Enter the number of paper bags."))
    sweets = int(input("Enter the number of sweets, it must be greater than the number of paper bags."))
    if sweets <= bags:
        print("Number of sweets is not greater than number of paper bags, retry.")
    else:
        valid = True

if (sweets - bags) % 2 == 0:
    print("An odd number of sweets can be placed in each bag")
else:
    print("An odd number of sweets cannot be placed in each bag")