import gc

# class Node:
#     def __init__(self,next=None,prev=None,data=None):
#         self.next = next
#         self.prev = prev
#         self.data = data

#     #add node at the front of list
#     def push(self,new_data):
#         new_node = Node(data=new_data)
#         new_node.next = self.head
#         new_node.prev = None

#         if self.head is not None:
#             self.head.prev = new_node
#         self.head = new_node

#     #insert after a node
#     def insertAfter(self,prev_node,new_data):
#         if prev_node is None:
#             print('this node doesn\'t exist')
#             return

#         new_node = Node(data=new_data)

#         new_node.next = prev_node.next

#         prev_node.next = new_node
#         new_node.prev = prev_node

#         if new_node.next is not None:
#             new_node.next.prev = new_node

#     #add node at the end
#     def append(self,new_data):
#         new_node = Node(new_data)

#         last = self.head
#         new_node.next=None

#         #if linked list is empty
#         if self.head is None:
#             new_node.prev = None
#             self.head = new_node
#             return

#         while last.next is not None:
#             last = last.next

#         last.next = new_node
#         new_node.prev = last


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # add node at the front of list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    # insert a node after a given node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print('previous node is not NULL')
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    # add node at the end
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

        new_node.prev = last

        return

    # delete a node in a doubly linked list
    def deleteNode(self, dele):

        if self.head is None or dele is Node:
            return

        if self.head == dele:
            self.head = dele.next

        if dele.next is not None:
            dele.next.prev = dele.prev

        if dele.prev is not None:
            dele.prev.next = dele.next

        gc.collect()

    # reverse a doubly linked list

    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev

    ### reverse method--2 ###
    # reverse using stacks

    def reverseStacks(self):
        stack = []
        temp = self.head
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next

        while temp is not None:
            temp.data = stack.pop()
            temp = temp.next

    # print list

    def printList(self, node):
        print('traversal in forward direction')
        while node:
            print(node.data, end=' ')
            last = node
            node = node.next

        print('traverasal in reverse direction')
        while last:
            print(last.data, end=' ')
            last = last.prev


if __name__ == "__main__":
    li = DoubleLinkedList()
    li.append(6)
    li.push(7)
    li.push(1)
    li.append(4)
    li.insertAfter(li.head.next, 8)
    li.printList(li.head)
    # li.deleteNode(li.head)
    li.printList(li.head)
    li.reverse()
    print(li.head)
