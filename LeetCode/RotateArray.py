# def rotate(arr, n):
#    list_1 = (arr[-n:] + arr[:-n])

#    return list_1


# nums = [-1,-100,3,99]
# k = 2
# print(rotate(nums, k))


def rotate(start, end, arr):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
l = len(arr)
nums = rotate(0, k-1, arr)
nums = rotate(k+1, l-1, arr)
nums = rotate(0, l-1, arr)
print(nums)

