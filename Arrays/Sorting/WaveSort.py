def sortInWave(arr,n):

    arr.sort()
    print(arr)


    for i in range(0,n-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr


arr = [10, 90, 49, 2, 1, 5, 23]
print(sortInWave(arr, len(arr)))