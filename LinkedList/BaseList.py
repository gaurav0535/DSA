class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class SLinkedList:
    def __init__(self):
        self.head = None

    def trav(self):

        printval = self.head
        if(printval):

            if(printval.next == None):
                print(printval.data)
            else:
                while(printval.next != None):
                    #print(printval.data)
                    printval = printval.next
                print(printval.data)

        else:
            print("Nothing is in linked list ")


l = SLinkedList()
l.head = Node(1)
n = Node(2)
n1 = Node(3)
n2 = Node(4)
n3 = Node(5)
n4 = Node(6)
l.head.next = n
n.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

l1 = SLinkedList()
l1.head = Node(2)

l.trav()
#print("Before big one")
#l.trav()
#print("after last ")
#SLinkedList().trav()





