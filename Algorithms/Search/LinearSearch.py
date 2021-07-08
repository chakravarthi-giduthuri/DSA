# def search(arr, n, x):
#     for i in range(0, n):
#         if arr[i] == x:
#             return i
#     return -1


# if __name__ == '__main__':
#     arr = [2, 3, 4, 10, 40]
#     n = len(arr)
#     x = 100

#     result = search(arr, n, x)

#     if result == -1:
#         print('element is not present in array')
#     else:
#         print('element is present at index', result)


def search(arr,x):
    left = 0
    length = len(arr)
    position = -1
    right = length-1

    for left in range(0,right,1):
        if arr[left] == x:
            postion = left
            print('element found in array at',position+1,'position with',left+1,'attempt')
            break
        
        if arr[right] == x:
            postion = right
            print('element found in array at',position+1,'position with',length-right,'attempt')
            break
        
        left +=1
        right-=1

        
