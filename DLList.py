class Node:
    def __init__(self,next=None,prev=None,data=None):
        self.next = next
        self.prev = prev
        self.data = data
    
    #add node at the front of list
    def push(self,new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    #insert after a node
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print('this node doesn\'t exist')
            return
        
        new_node = Node(data=new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    #add node at the end
    def append(self,new_data):
        new_node = Node(new_data)

        last = self.head
        new_node.next=None

        #if linked list is empty
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        
        while last.next is not None:
            last = last.next
        
        last.next = new_node
        new_node.prev = last

        
