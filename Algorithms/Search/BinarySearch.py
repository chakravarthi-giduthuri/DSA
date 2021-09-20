# def binarySearch(arr, l, r, x):
#     if r >= l:
#         mid = l+(r-1)//2

#         if arr[mid] == x:
#             return mid

#         elif arr[mid] > x:
#             return binarySearch(arr, l, mid-1, x)
#         else:
#             return binarySearch(arr, mid+1, r, x)
#     else:
#         return -1


# arr = [2, 3, 4, 10, 40]
# x = 10

# result = binarySearch(arr, 0, len(arr)-1, x)

# if result != -1:
#     print('element is present at index', result)
# else:
#     print('element is not present in array')





###### iterative method of binary search

def binarySearch(arr,l,r,x):
    while l<=r:
        
        mid = l +(r-l)//2

        if arr[mid] == x:
            return mid
        elif arr[mid]<x:
            l = mid+1
        else:
            r = mid-1

    return -1


arr = [2,3,4,10,40]
x = 40
result = binarySearch(arr,0,len(arr),x)
if result != -1:
    print('element is present at index',result)
else:
    print('element is not present in array')