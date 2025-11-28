
'''
{
    "left": 2,
    "data":"K",
    "right: -1 # dictionray representation of a node
}
tree[0]["data"] # how to access a key value pair (dictionary) node
tree[0][1] # how to access data in a 2d list (array) node
tree[0].data # how to access data in a object (or record) node
'''

# array2dTree = [
#     [1,"K",3],
#     [7,"E",2],
#     [-1,"H",-1],
#     [5,"R",4],
#     [6,"U",9],
#     [-1,"N",-1],
#     [-1,"T",-1],
#     [-1,"B",8],
#     [-1,"C",-1],
#     [-1,"Z",-1]
#     ]

class Node:
    def __init__(self, theleft, thedata, theright):
        self.data = thedata
        self.left = theleft
        self.right = theright

objectTree = [
    Node(1,"K",3),
    Node(7,"E",2),
    Node(-1,"H",-1),
    Node(5,"R",4),
    Node(6,"U",9),
    Node(-1,"N",-1),
    Node(-1,"T",-1),
    Node(-1,"B",8),
    Node(-1,"C",-1),
    Node(-1,"Z",-1)
    ]

print(objectTree)
print(objectTree[0].data)

def traverse(data):
    if objectTree[data].left != -1:
        traverse(objectTree[data].left)
    print(objectTree[data].data)
    if objectTree[data].right != -1:
        traverse(objectTree[data].right)
traverse(2)