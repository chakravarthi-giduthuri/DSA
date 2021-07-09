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


def search(arr, x):
    left = 0
    length = len(arr)
    position = -1
    right = length-1

    for left in range(0, right, 1):
        if arr[left] == x:
            position = left
            print('element found in array at', position +
                  1, 'position with', left+1, 'attempt')
            break

        if arr[right] == x:
            position = right
            print('element found in array at', position+1,
                  'position with', length-right, 'attempt')
            break

        left += 1
        right -= 1

    if position == -1:
        print('not found in array with', left, 'attempt')


arr = [1, 2, 3, 4, 5]
x = 4
search(arr, x)
