def fixArray(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[j] == i:
                arr[j], arr[i] = arr[i], arr[j]
    # return arr

    for i in range(n):
        if arr[i] != i:
            arr[i] = -1
    print('array after rearranging')
    for i in range(n):
        print(arr[i], end=' ')


arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
n = len(arr)

print(fixArray(arr, n))
