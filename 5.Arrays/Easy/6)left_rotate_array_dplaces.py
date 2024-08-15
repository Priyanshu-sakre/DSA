# less time
def rotate_array(n, arr, k):
    temp = arr[0:k]
    for i in range(k, n):
        arr[i - k] = arr[i]
    for i in range(n - k, n):
        arr[i] = temp[i - (n - k)]
    return arr


arr = [1, 2, 3, 4, 5]
n = len(arr)
print(rotate_array(n, arr, 3))


# more time
def rotate_array2(n, arr, k):
    for i in range(k):
        temp = arr[0]
        for i in range(1, n):
            arr[i - 1] = arr[i]
        arr[n - 1] = temp
    return arr


arr2 = [1, 2, 3, 4, 5]
n = len(arr2)
print(rotate_array2(n, arr2, 3))


# reverse fn
def reverse1(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array3( arr, k):
    reverse1(arr, 0, k - 1)
    reverse1(arr, k, len(arr) - 1)
    reverse1(arr, 0, len(arr) - 1)
    return arr


arr3 = [1, 2, 3, 4, 5, 6, 7]
print(rotate_array3(arr3, 3))
