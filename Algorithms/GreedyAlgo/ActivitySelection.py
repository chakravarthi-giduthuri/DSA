# def printMaxActivites(s, f):
#     n = len(f)
#     print('following activities are selected')

#     i = 0
#     print(i)

#     for j in range(n):
#         if s[j] >= f[j]:
#             print(j)
#             i = j


# s = [1, 3, 0, 5, 8, 5]
# f = [2, 4, 6, 7, 9, 9]

# printMaxActivites(s, f)



def MaxActivities(arr,n):
    selected = []

    Activity.sort(key = lambda x :x[1])

    i=0
    selected.append(arr[i])
    for j in range(1,n):
        if arr[j][0]>=arr[i][1]:
            selected.append(arr[j])
            i=j

    return selected


Activity = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
n = len(Activity)
selected = MaxActivities(Activity, n)
print("Following activities are selected :")
print(selected)
