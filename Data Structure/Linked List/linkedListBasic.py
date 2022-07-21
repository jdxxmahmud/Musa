class Node:
        def __init__(self, parameterValue):
                self.val = parameterValue
                self.next = None
                self.onCreateNode()
        
        def onCreateNode(self):
                print("Node has been created:", self.val)


new_node1 = Node(5)

print(new_node1.val)
new_node2 = Node(7)

new_node1.next = new_node2
print(new_node2.val)
# print("Address of new_node1.next:",new_node1.next)
# print("Address of new_node2:",new_node2)

new_node3 = Node(2)
new_node2.next = new_node3

