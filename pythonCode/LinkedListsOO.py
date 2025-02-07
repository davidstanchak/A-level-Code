class Node():
    def __init__(self, given_data):
        """Constructor method"""
        self.data = given_data
        self.next = None
        
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next


class LinkedList():
    def __init__(self, current):
        """Constructor method"""
        self.head = None
        print("Head pointer Memory Address: ", current)

    def traverse(self, my_list):
        # Set the current node as the head
        current = self.head
        # Repeat until there are no more linked nodes
        while current is not None:
            print(current.get_data())
            current = current.get_next()
    
    def insert_at_front(self, data):

        

my_list.insert_at_front("David")

# Instantiate an empty linked list object
my_list = LinkedList()
print(my_list.head)