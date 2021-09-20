def square(arr):
    x = []
    for i in range(len(arr)):
        y = arr[i]*arr[i]
        x.append(y)
        x.sort()
    return x


arr = [-7,-3,2,3,11]
print(square(arr))
