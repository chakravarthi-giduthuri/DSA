def rotate(arr, n):
    temp = arr[n-1]

    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=',')


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    rotate(arr, len(arr))
    printArray(arr)
