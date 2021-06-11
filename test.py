# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.nxt = None


# class linkList:
#     def __init__(self):
#         self.head = None

#     def printList(self):
#         temp = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.nxt


# li = linkList()
# li.head = Node(1)
# second = Node(2)
# third = Node(3)

# li.head.nxt = second
# second.nxt = third

# li.printList()

# # print(li.head.data)
# # print(li.head.nxt.data)
# # print(li.head.nxt.data)


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None



if __name__=='__main__':
    li = linkedList()
    li.head = Node(1)
    