class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head = None

    def trav(self):

        printval = self.head
        if(printval):

            if(printval.next == None):
                print(printval.data)
            else:
                while(printval != None):
                    print(printval.data)
                    printval = printval.next

        else:
            print("Nothing is in linked list ")


    def middle(self,):
        first = self.head
        second = self.head

        while  first !=None and first.next != None:
            print("Fast ptr",first.data)
            print("Slow ptr", second.data)
            first = first.next.next
            second = second.next
        print(second.data)

SList = SlinkedList()
SList.head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

#   1 2 3 4 5 6 7 8


SList.head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
#n7.next = n8
#SList.trav()
SList.middle()



