def leftRotate(arr, d, n):
    for i in range(d):
        rotateOne(arr, n)


def rotateOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp


def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=' ')


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    leftRotate(arr, 2, len(arr))
    printArray(arr, len(arr))
