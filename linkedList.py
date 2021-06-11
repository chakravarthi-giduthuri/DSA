#Node class
class Node:
    #func to initialze the node object
    def __init__(self,data):
        self.data = data
        self.next = None



#Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
    
    #add a node at the front of list
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    #add a node after the given prev node
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print('the given previous node must linkedlist')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    #add a node at the end
    def append(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node

    #delete node
    def delete(self,key):
        temp = self.head

        # if head is the key to be delete
        if temp is not None:
            if temp.data ==key:
                self.head = temp.next
                temp = None
                return
    
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return
        
        prev.next = temp.next
        temp = None


    # delete total linked list
    def deleteList(self):
        
        #initialize the current node
        current = self.head
        
        while current:
            #move to next node
            prev = current.next 

            #delete the current node
            del current.data

            #set set equals to prev node 
            current = prev



            
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



#code execution


if __name__ =='__main__':
    li = LinkedList()
    li.append(6)
    li.push(7)
    li.push(1)
    li.append(4)
    li.append(3)
    li.delete(7)
    li.insertAfter(li.head.next,8)
    print('created list is')
    li.printList()
    li.deleteList()
    print('list is deleted')

