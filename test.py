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


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class linkedList:
#     def __init__(self):
#         self.head = None


# if __name__=='__main__':
#     li = linkedList()
#     li.head = Node(1)

# print(2%5)


# ar = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

# for i in range(len(ar)):
#     for j in range(len(ar)):
#         if ar[j] == i:
#             ar[j],ar[i]=ar[i],ar[j]
# print(ar)


arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
for i in range(n):
    for j in range(0, n-i):
        print(j, end=',')
    print()
