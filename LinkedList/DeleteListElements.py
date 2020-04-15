# Build node
class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class SLinkedList:
    def __init__(self):
        self.head = None

    def deleteE(self,pos):
        count = 1
        pos = pos -1
        current = self.head
        while(count < pos):
            current = current.next
            count = count + 1

        current.next = current.next.next
        print(current.data)
        print(count)
    def printlist(self):
        printl = self.head
        while (printl != None):
            print(printl.data)
            printl = printl.next

list = SLinkedList()
list.head = Node(1)
list.head.next = Node(2)
list.head.next.next = Node(3)
list.head.next.next.next = Node(4)
list.head.next.next.next.next = Node(5)

#list.printlist()


list.deleteE(5)

print("After deleting")
list.printlist()


