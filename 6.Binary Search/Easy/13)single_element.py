# brute
def single_element(arr):
    if len(arr) == 1:
        return arr[0]
    for i in range(len(arr)):
        if i == 0:
            if arr[i] != arr[i + 1]:
                return arr[i]
        elif i == len(arr) - 1:
            if arr[i] != arr[i - 1]:
                return arr[i]
        else:
            if arr[i] != arr[i + 1] and arr[i] != arr[i - 1]:
                return arr[i]


arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
print(single_element(arr))


# binary_search
def element(arr):
    if len(arr) == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[len(arr) - 1] != arr[len(arr) - 2]:
        return arr[len(arr) - 1]
    low = 1
    high = len(arr) - 2
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (
            mid % 2 == 0 and arr[mid] == arr[mid + 1]
        ):
            low = mid + 1
        else:
            high = mid - 1


arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
print(element(arr))
