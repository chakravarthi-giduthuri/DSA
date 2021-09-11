# -------> ITERATIVE METHOD <-------


# def reverseList(arr, start, end):
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1


# arr = [1, 2, 3, 4, 5, 6]
# print(arr)
# reverseList(arr, 0, 5)
# print("Reversed list is")
# print(arr)



#------>RECURSIVE METHOD <------

def reverseList(arr,start,end):
    if start >= end:
        return
    
    arr[start],arr[end] = arr[end],arr[start]
    reverseList(arr,start+1,end-1)

arr = [1, 2, 3, 4, 5, 6]
print(arr)
reverseList(arr, 0, 5)
print("Reversed list is")
print(arr)

