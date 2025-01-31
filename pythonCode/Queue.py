busQueue = [None,None,None,None,None,] #empty array of 5 elements
front = 0 #points at first item in the queue
rear = -1 #points at last element in queue, -1 means empty
size = 0
maxSize = 5

def enQueue(item):
    global front, size, rear
    #add item to queue
    print("front: ",front,"rear: ",rear,"\n")
    if isFull():
        print("Sorry Queue is full")
    else:
        
        rear = (rear+1) % maxSize
        size += 1
        busQueue[rear] = item
        print(f"You have Enqueued: {item}\n")

def deQueue():
    global front, size, rear
    print("front: ",front,"rear: ",rear,"\n")
    #change front pointer +1
    #return item
    if isEmpty():
        print("THe queue is already empty \n")
    else:
        # dequeue from the front
        currentFront = busQueue[front]
        busQueue[front] = None
        front += 1
        size -= 1
        print(f"{currentFront} has left the queue \n")

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
print(busQueue)
enQueue(21)
print(busQueue)
enQueue(1000)
print(busQueue)
enQueue(4)
print(busQueue)
enQueue(19)
print(busQueue)
deQueue()
print(busQueue)
enQueue(900)
print(busQueue)
deQueue()
print(busQueue)
deQueue()
print(busQueue)
deQueue()
print(busQueue)
enQueue(901)
print(busQueue)
