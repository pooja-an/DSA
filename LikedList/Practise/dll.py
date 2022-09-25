class Node:

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedlist:

    def __init__(self):
        self.head = None

#----------------------------------------------------
    # insert node at begining
    def insert_node_at_beginning(self, data):
        node = Node(data, prev=None, next=self.head)
        if self.head is None:
            self.head = node
        self.head.prev = node
        self.head = node
    

#----------------------------------------------------
    # insert node at end
    def insert_at_end(self, data):

        node = Node(data)

        if self.head is None:
            self.head = node
            return

        temp = self.head
        
        while temp.next:
            temp = temp.next

        temp.next = node
        node.prev = temp

#----------------------------------------------------
        
    # insert node after a given node

    def insert_after_node(self, value, data):

        if self.head is None:
            print('Linked list is empty')
            return        

        temp = self.head

        while temp.data != value:
            temp = temp.next

        node = Node(data, prev=temp, next=temp.next)
        temp.next = node

#----------------------------------------------------
    # insert node before a given node

    def insert_before_node(self, value, data):

        if self.head is None:
            print('Linked list is empty')
            return
        
        if self.head.data == value:
            head.insert_node_at_beginning(data)
            return        

        temp = self.head
        
        while temp.next.data != value:
            temp = temp.next

        node = Node(data, prev=temp, next=temp.next)
        temp.next = node

#----------------------------------------------------
    # Insert at given index
    def insert_at_index(self, index, data):

        size = self.get_length()

        if index > (size - 1):
            print('Invalid Index')
            return

        if index == 0:
            self.insert_node_at_beginning(data)
            return

        count = 0
        temp = self.head

        while count != index -1:
            count += 1
            temp = temp.next

        node = Node(data, temp, temp.next)
        temp.next = node
        return

        
#----------------------------------------------------
    # Find the length of the linked list
    def get_length(self):

        size = 0
        if self.head is None:
            return size
        temp = self.head

        while temp:
            size += 1
            temp= temp.next
            
        return size
#----------------------------------------------------
    # Print the linked list

    def print(self):
        if self.head is None:
            print("Linked list is empty...")

        ll = ''

        temp = self.head

        while temp:
            ll += str(temp.data) + '-->'
            temp = temp.next
            
        print(ll)
#----------------------------------------------------
    # Create a normal linked list from a list of data

    def create_list(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

#----------------------------------------------------
    # Add a node in the list

    def add_node(self, data):
        self.insert_at_end(data)
        
#----------------------------------------------------
    # Remove given node

    def remove_node(self, data):

        if self.head is None:
            print('Linked list is empty...')
            return

        if self.head.data == data:
            node = self.head.next
            self.head = node
            return

        temp = self.head

        while temp.next.data != data:
            temp = temp.next

        node = temp.next
        temp.next = temp.next.next
                
#----------------------------------------------------
    # Print the linked list

    def print(self):
        if self.head is None:
            print("Linked list is empty...")

        ll = ''

        temp = self.head

        while temp:
            ll += str(temp.data) + '-->'
            temp = temp.next
            
        print(ll)
#------------------------------------------------------
    # Print linked list in reverse direction. Use node.prev for this.
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty...")

        ll = ''
        temp = self.head

        while temp.next:
            temp = temp.next
            
        while temp:
            ll += str(temp.data) + '-->'
            temp = temp.prev
            
        print(ll)        
#------------------------------------------------------        
head = DoublyLinkedlist()
head.insert_node_at_beginning(10)
head.insert_node_at_beginning(20)
head.insert_node_at_beginning(30)
head.print()
head.insert_after_node(20,5)
head.print()
head.remove_node(5)
head.print()
head.print_backward()