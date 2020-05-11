#Define Node
class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

#Define SinglyLinkedList
class SLinkedList:
    def __init__(self):
        self.head = None

    def lsitprint(self):
        #print the all elements of the list
        current = self.head
        while(current.next != None):
                print(current.data)
                current = current.next

    def begning(self,data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

list = SLinkedList()
list.head = Node("1")
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l5 = Node(5)

list.head.next = l2
l2.next = l3
l3.next = l4
l4.next =l5

list.lsitprint()

list.begning(0)
list.begning(-1)
print("Inserting new element")

list.lsitprint()




