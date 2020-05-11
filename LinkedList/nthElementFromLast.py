class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SlinkedList:
    def __init__(self):
        self.head = None


    def nthFromLast(self,n):
        first = self.head
        second = self.head
        printl = self.head
        length = 0
        i = 0

        while (printl != None):
            printl = printl.next
            length = length + 1

        if length > 0:
            if n <= length:
                while(i < n):
                    second = second.next
                    i = i + 1

                while(second != None ):
                    first = first.next
                    second = second.next
                print(first.data)
            else:
                print("Given digit is greater than the asked one our linkedlist is of length {}".format(length))
        else:
            print("Linked List is empty")


l = SlinkedList()
l.head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

l.head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

l.nthFromLast(8)
# Lets print the second last element from the linked list



