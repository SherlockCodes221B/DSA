class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None


    ## Insert at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    ## Insert at the Last
    def insertAtLast(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_data
            return
        last = self.next
        while last.next:
            last = last.next
        last.next = new_node

    def print_data(self):
        temp = self.head
        while temp:
            print(temp.data, end = '')
            temp = temp.next
        print()
