def sumOfPair(arr, n, x):
    arr.sort()

    # for i in range(0, n-1):
    #     if arr[i] > arr[i+1]:
    #         break

    # l = (i+1) % n
    # r = i
    l=0
    r=n-1
   
    

    while l < r:
        if arr[l]+arr[r] == x:
            return True
        if arr[l]+arr[r] < x:
            l +=1
        else:
            r -=1
    return False


arr = [11, 15, 6, 8, 9, 10]
sum = 16
n = len(arr)
print(sumOfPair(arr, n, sum))

# if (sumOfPair(arr, n, sum)):
#     print("Array has two elements with sum 16")
# else:
#     print("Array doesn't have two elements with sum 16 ")
