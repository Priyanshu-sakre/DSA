# more TC
arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]


def zeros(arr, n):
    temp = []
    for i in arr:
        if i != 0:
            temp.append(i)
    for i in range(len(temp)):
        arr[i] = temp[i]
    for i in range(len(temp), n):
        arr[i] = 0
    del temp
    return arr


n = len(arr)
print(zeros(arr, n))


# less TC
def zeros2(n, arr):
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr


print(zeros2(n, arr))
