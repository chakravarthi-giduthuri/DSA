def printLeader(arr, size):
    max_from_right = arr[size-1]
    print(max_from_right)
    for i in range(size-1, -1, -1):
        if max_from_right < arr[i]:
            print(arr[i])
            max_from_right = arr[i]


arr = [16, 17, 4, 3, 5, 2]
printLeader(arr, len(arr))
