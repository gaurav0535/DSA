# Build single node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Build LinkedList
class SlinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self,from_node,data):
        current  = self.head

        while(current.data !=from_node ):
            current =current.next
        newN = Node(data)
        newN.next = current.next
        current.next = newN

    def printlist(self):
        current = self.head
        while(current != None):
            print(current.data)
            current =current.next


list = SlinkedList()
list.head = Node(1)
list.head.next = Node(2)
list.head.next.next = Node(3)
list.head.next.next.next = Node(4)
list.head.next.next.next.next = Node(5)

list.printlist()

list.insertNode(2,2.5)

print("After insertion ")

list.printlist()





