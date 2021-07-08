import array as a
import numpy as np

def rearrange(arr,n):
    evenpos = n/2
    oddpos = n-evenpos

    tempArr = np.empty(n,dtype=object)

    for i in range(0,n):
        tempArr[i] = arr[i]

    tempArr.sort()

    j = oddpos-1

    for i in range(0,n,2):
        arr[i] = tempArr[j]
        j = j-1

    j = oddpos

    for i in range(1,n,2):
        arr[i] = tempArr[j]
        j = j+1

    for i in range(0,n):
        print(arr[i],end=' ')



arr = a.array('i', [ 1, 2, 3, 4, 5, 6, 7 ])
rearrange(arr, 7)

