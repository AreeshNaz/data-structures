class Node:
    def _init_(self, d):
        self.data = d
        self.next = None  

# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# creating link
head = node1 
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
print_linked_list(head)