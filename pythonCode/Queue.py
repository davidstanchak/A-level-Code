busQueue = [None,None,None,None,None,] #empty array of 5 elements
front = 0 #points at first item in the queue
rear = -1 #points at last element in queue, -1 means empty
size = 0
maxSize = 5

def enQueue(item):
    global front, size, rear
    #add item to queue
    if isFull(): 
        print("Sorry Queue is full")
        return
    else:
        busQueue[rear] = item
        rear += 1
        print(f"You have Enqueued: {item}")

def deQueue():
    #change front pointer +1
    #return item
    if isEmpty():
        print("THe queue is already empty")
    else:
        # dequeue from the front
        currentFront = busQueue[front]
        front += 1
        return currentFront

def isFull():
    #check if queue is full
    if size == maxSize:
        return True
    else:
        return False

def isEmpty():
    #check if queue is empty
    if size == 0:
        return True
    else:
        return False

enQueue(255)
enQueue(21)
enQueue(1000)
enQueue(4)
enQueue(19)
enQueue(12)

print(busQueue)