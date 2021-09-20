def rearrange(arr, n):
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    print(arr)
    pos,neg = i+1,0
    while pos<n and neg<pos and arr[neg]<0:
        arr[neg],arr[pos] = arr[pos],arr[neg]
        pos+=1
        neg+=2
    return arr

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]


n = len(arr)
print(rearrange(arr, n))
