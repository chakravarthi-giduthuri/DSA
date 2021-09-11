def reArrange(arr, n, x):
    m = {}

    for i in range(n):
        m[arr[i]] = abs(x-arr[i])

    m = {k: v for k, v in sorted(m.items(), key=lambda item: item[1])}

    # return m
    
    i = 0
    for it in m.keys():
        arr[i] = it
        i+=1
    return arr


if __name__ == "__main__":

    arr = [10, 5, 3, 9, 2]
    n = len(arr)
    x = 7
    print(reArrange(arr, n, x))
    # printArray(arr, n)
