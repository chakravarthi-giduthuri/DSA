def alternateSort(arr,n):
    arr.sort()

    i = 0
    j = n-1

    while i<j:
        print(arr[j],end=' ')
        j-=1
        print(arr[i],end=' ')
        i+=1
    # If the total element in array is odd
    # then print the last middle element.
    if (n % 2 != 0):
        print(arr[i])
    

arr = [1, 12, 4, 6, 7, 10]
n = len(arr)
 
alternateSort(arr, n)