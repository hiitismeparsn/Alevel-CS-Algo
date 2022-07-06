

class Node:
    def __init__(self,data=None):
        self.data = data
        self.nextptr = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):    #Append data to the end of the list
        current = self
        while current.nextptr != None:
            current = current.nextptr
        current.nextptr = Node(data)

    def prepend(self,data): #Replace the head of the list
        newnode = Node(data)    #Create a new node that will become the head
        newnode.nextptr = self.head #Assign the newnodes pointer to the value of the header
        newnode = self.head #Replace the head as newnode



MyList = LinkedList()
Node10 = Node(10)
MyList.append(Node10)