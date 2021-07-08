def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1
    print(arr)
A = [1, 2, 3, 4, 5, 6]

reverse(A,0,len(A)-1)

