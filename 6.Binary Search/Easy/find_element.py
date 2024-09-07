# iterative
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [-1, 0, 3, 5, 9, 12]
target = 9
print(binary_search(arr, target))


# recursive
def binary_search2(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search2(arr, mid + 1, high, target)
    else:
        return binary_search2(arr, low, mid - 1, target)


def search(arr, target):
    return binary_search2(arr, 0, len(arr) - 1, target)


print(search(arr, target))
