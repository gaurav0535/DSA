class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head

        while(printval != None):
            print(printval.data)
            printval = printval.next


list = SLinkedList()
list.head = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

#Now link the nodes to form proper linked list

list.head.next =e2
e2.next = e3
e3.next = e4
e4.next = e5

list.listprint()