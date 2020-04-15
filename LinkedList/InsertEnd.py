class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SlinkedList:
    def __init__(self):
        self.head = Node

# Function to add new element at the start
    def insertBeg(self,data):
        newN = Node(data)
        newN.next = self.head
        self.head = newN

# Function to add new element at the end

    def insertEnd(self,data):
        newE = Node(data)
        current = self.head
        while (current.next != None):
            current = current.next
        current.next = newE

    def printlist(self):
        printl = self.head
        while (printl != None):
            print(printl.data)
            printl = printl.next


list = SlinkedList()
list.head = Node(0)
l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l5 = Node(5)

list.head.next = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

list.insertEnd(6)
list.insertEnd(7)
list.insertEnd(8)
list.insertEnd(9)
list.insertBeg(-1)

list.printlist()
