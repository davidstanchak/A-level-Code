array = [None]*10
top = -1

def isEmpty():
    global top 
    if top == -1:
        return True
    else:
        return False

def isFull():
    global top 
    if top+1 == 10:
        return False

def push(item):
    global top 
    if not isFull():
        top += 1
        array[top] = item
    else:
        print("Stack overflow")
    return array

def pop():
    global top
    if not isEmpty():
        popItem = array[top]
        top -= 1
        return popItem
    else:
        print("Stack underflow")

push("bob")
push("jeff")

reversedStack = [None]*(top+1)
stack = [None]*(top+1)

for i in range(top+1):
    stack[i] = array[i]

for i in range(top+1):
    reversedStack[i] = pop()
print(reversedStack)

    



