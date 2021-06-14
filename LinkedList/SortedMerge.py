#linked list node



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


#link operations
class LinkedList:
    def __init__(self):
        self.head = None


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
    
    #method to add element to list

    def addToList(self,newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    
#function to merge the lists
#take 2 sorted lists and join them to a singel list

def mergeList(headA,headB):
    #dummy node to store the result
    dummyNode = Node(0)

    #tail stores the last node
    tail = dummyNode

    while True:
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        if headA.data<=headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
        tail = tail.next
    
    return dummyNode.next

listA = LinkedList()
listB = LinkedList()

listA.addToList(5)
listA.addToList(10)
listA.addToList(15)

listB.addToList(2)
listB.addToList(3)
listB.addToList(20)


listA.head = mergeList(listA.head,listB.head)
# print('merged Linked list is')
# listA.printList()


#recursive method

def mergeLists(head1,head2):
    temp = None

    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        temp = head1
        temp.next = mergeLists(head1.next,head2)
    else:
        temp = head2
        temp.next = mergeLists(head1,head2.next)
    return temp


if __name__ == "__main__":
    list1 = LinkedList()
    list1.addToList(10)
    list1.addToList(20)
    list1.addToList(30)
    list1.addToList(40)
    list1.addToList(50)

    list2 = LinkedList()
    list2.addToList(5)
    list2.addToList(15)
    list2.addToList(18)
    list2.addToList(35)
    list2.addToList(60)


    list3 = LinkedList()
    list3.head = mergeLists(list1.head,list2.head)
    list3.printList()