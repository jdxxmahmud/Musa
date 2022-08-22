from urllib.parse import non_hierarchical


class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

head = None

def printList(head):
    currentNode = head 
    print('The elements of the list are:', end = "")

    while currentNode is not None:
        print(currentNode)
        currentNode = currentNode.next 

    
def appendNode(head: Node, val: int):

    if head is None:
        head = Node(val)

    else:
        newNode = Node(val)
        currentNode = head 

        while currentNode.next is not None:
            currentNode = currentNode.next

            currentNode.next = newNode

        
    return head 


head = appendNode(head, 4)
head = appendNode(head, 2)
head = appendNode(head, 1)
head = appendNode(head, 7)
head = appendNode(head, 12)

printList(head)
