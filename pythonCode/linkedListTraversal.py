names = ["Jeff", "Harry", "Sam", "Daniel", "Oscar"]
data = 0
pointer = 1

first = 3
nextFree = 5

linkedList = [
    ["John", 1],
    ["Harry", None],
    ["Sam", 0],
    ["Daniel", 4],
    ["Oscar", 2],
    [None, None]
    ]

current = first
while current != None:
    print(linkedList[current][data])
    current = linkedList[current][pointer]