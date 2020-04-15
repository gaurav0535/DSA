class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head = None

list1 = SlinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thursday")
e5 = Node("Friday")

#Link first Node to Second node

list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5






