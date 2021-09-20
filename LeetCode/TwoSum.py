# def twoSum(arr, target):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i] + arr[j] == target:
#                 return [i+1, j+1]


# def twoSum(arr, target):
#     required = {}
#     for i in range(len(arr)):
#         if target-arr[i] in required:
#             return [required[target-arr[i]]+1, i+1]
#         else:
#             required[arr[i]] = i


def twoSum(arr,target):
    left= 0
    right = len(arr)-1
    while left <right:
        x = target-arr[left]

        if arr[right] == target :
            break
        elif numbers[right]<x:
            left+=1
        else:
            right-=1
    return [left+1,right+1]


numbers = [0, 0, 1, 2]
target = 0

print(twoSum(numbers, target))


