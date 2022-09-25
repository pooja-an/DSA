class Node:

    def __init__(self, data, next=None):

        self.data = data
        self.next = next

    def __str__(self):
        print(self.data,'->',self.next)

class Linkedlist:

    # Create linked list object
    def __init__(self):
        self.head = None

#----------------------------------------------------
    # insert node at begining
    def insert_node_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

#----------------------------------------------------
    # insert node at end
    def insert_at_end(self,data):

        node = Node(data)

        if self.head is None:
            self.head = node
            return

        temp = self.head
        
        while temp.next:
            temp = temp.next

        temp.next = node

#----------------------------------------------------
        
    # insert node after a given node

    def insert_after_node(self, value, data):

        if self.head is None:
            print('Linked list is empty')
            return        

        temp = self.head

        while temp.data != value:
            temp = temp.next

        node = Node(data, temp.next)
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

        node = Node(data, temp.next)
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

        node = Node(data, temp.next)
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

    def deleteDuplicates(self):
        
        if self.head == None or self.head.next == None:
            return head
        
        prev = self.head
        temp = self.head.next
                
        while temp:
    
            if prev.data == temp.data:
                temp = temp.next
                
            else:
                prev.next = temp 
                prev = temp
                temp = temp.next

        prev.next = None
                
        return self.head        
        
#----------------------------------------------------               
dataList = [1,1,2,3,3]
head = Linkedlist()
head.create_list(dataList)
head.print()
head.deleteDuplicates()
head.print()

        
