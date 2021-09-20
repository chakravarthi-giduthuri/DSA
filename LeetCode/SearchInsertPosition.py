# # def Search(arr, target):
# #     left = 0
# #     right = len(arr)

# #     while left <= right:
# #         mid = left + (right-left)//2
# #         if arr[mid] == target:
# #             return mid
# #         elif arr[mid] > target:
# #             right = mid-1
# #         else:
# #             left = mid+1

# #     return Insert(arr, target)

# def Search(arr,target):
#     l = 0
#     r = len(arr)
#     while l<=r:

#         mid = l +(r-l)//2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid]<target:
#             l = mid+1
#         else:
#             r = mid-1

#     arr.append(target)
#     arr.sort
#     return Search(arr,target)

#     # return Insert(arr,target)


# def Insert(arr, target):
#     arr.append(target)
#     arr.sort
#     # # print(arr,target)
#     # for i in range(len(arr)):

#     #     # print(len(arr))
#     #     if arr[i] > target:
#     #         arr.insert(i, target)
#     #         break
#     #     else:
#     #         arr.append(target)

#     # arr.append(target)

#     return Search(arr, target)
#     # return arr, len(arr)


# arr = [1, 3, 5, 6]


# target =7
# print(Search(arr, target))


def Search(nums, target):
    left = 0
    right = len(nums) - 1
    print(left, right)
    while left <= right:
        mid = (left + right) // 2
        print(mid)
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left


arr = [1, 3, 5, 6]
target = 2
print(Search(arr, target))
