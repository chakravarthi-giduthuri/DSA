# Search an element in sorted and rotated array using
# single pass of Binary Search


def search(arr,low,high,key):
    if low > high:
        return -1

    mid = (low +high)//2
    if arr[mid] ==key:
        return mid
    
    ## IF ARRAY IS SORTED
    if arr[low]<=arr[mid]:
        if key>=arr[low] and key <=arr[mid]:
            return search(arr,low,mid-1,key)
        return search(arr,mid+1,high,key)
    
    if key>=arr[mid] and key <=arr[high]:
        return search(arr,mid+1,high,key)
    return search(arr,low,mid-1,key)


if __name__=='__main__':
    arr = [4,5,6,7,8,9,10,1,2,3]
    key = 6
    i = search(arr,0,len(arr),key)
    if i!=-1:
        print('index',i)
    else:
        print('key not found')
