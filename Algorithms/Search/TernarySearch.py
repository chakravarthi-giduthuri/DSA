def ternarySearch(l, r, key, arr):
    mid1 = l+(r-l)//2
    mid2 = r-(r-l)//2

    if key == mid1:
        return mid1

    if key == mid2:
        return mid2

    if key <= arr[mid1]:
        return ternarySearch(l, mid1-1, key, arr)
    elif key >= arr[mid2]:
        return ternarySearch(mid2+1, r, key, arr)
    else:
        return ternarySearch(mid1+1, mid2-1, key, arr)


ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Starting index
l = 0

# length of array
r = 9

# Checking for 5

# Key to be searched in the array
key = 8

# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)
