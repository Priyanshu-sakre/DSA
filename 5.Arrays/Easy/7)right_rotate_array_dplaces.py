# brute
def rotate_array(arr, k):
    for i in range(k):
        n = len(arr)
        temp = arr[n - 1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = temp
    return arr


arr2 = [1, 2, 3, 4, 5, 6, 7]
print(rotate_array(arr2, 3))


# using reverse function
def reverse1(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array3(arr, k):
    reverse1(arr, 0, len(arr) - 1)
    reverse1(arr, 0, k - 1)
    reverse1(arr, k, len(arr) - 1)

    return arr


arr3 = [1, 2, 3, 4, 5, 6, 7]
print(rotate_array3(arr3, 3))
